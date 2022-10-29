from __future__ import annotations
from logging import PlaceHolder

from rich.console import RenderableType
from rich.style import StyleType


from .. import events
from ..layouts.grid import GridLayout
from ..message import Message
from ..messages import UpdateMessage
from ..scrollbar import ScrollTo, ScrollBar
from ..geometry import clamp, Offset, Size
from ..page import Page
from ..reactive import watch
from ..view import View
from ..widget import Widget

from ..reactive import Reactive


class ScrollView(View):
    def __init__(
        self,
        contents: RenderableType | Widget | None = None,
        *,
        name: str | None = None,
        style: StyleType = "",
        fluid: bool = True,
    ) -> None:
        from ..views import WindowView

        self.fluid = fluid
        self.vscroll = ScrollBar(vertical=True)
        self.hscroll = ScrollBar(vertical=False)
        self.window = WindowView("" if contents is None else contents)
        layout = GridLayout()
        layout.add_column("main")
        layout.add_column("vscroll", size=1)
        layout.add_row("main")
        layout.add_row("hscroll", size=1)
        layout.add_areas(
            content="main,main", vscroll="vscroll,main", hscroll="main,hscroll"
        )
        layout.show_row("hscroll", False)
        layout.show_column("vscroll", False)
        super().__init__(name=name, layout=layout)

    x: Reactive[float] = Reactive(0, repaint=False)
    y: Reactive[float] = Reactive(0, repaint=False)

    target_x: Reactive[float] = Reactive(0, repaint=False)
    target_y: Reactive[float] = Reactive(0, repaint=False)

    def validate_x(self, value: float) -> float:
        return clamp(value, 0, self.max_scroll_x)

    def validate_target_x(self, value: float) -> float:
        return clamp(value, 0, self.max_scroll_x)

    def validate_y(self, value: float) -> float:
        return clamp(value, 0, self.max_scroll_y)

    def validate_target_y(self, value: float) -> float:
        return clamp(value, 0, self.max_scroll_y)

    @property
    def max_scroll_y(self) -> float:
        return max(0, self.window.virtual_size.height - self.size.height)

    @property
    def max_scroll_x(self) -> float:
        return max(0, self.window.virtual_size.width - self.size.width)

    async def watch_x(self, new_value: float) -> None:
        self.window.scroll_x = round(new_value)
        self.hscroll.position = round(new_value)

    async def watch_y(self, new_value: float) -> None:
        self.window.scroll_y = round(new_value)
        self.vscroll.position = round(new_value)

    async def update(self, renderable: RenderableType, home: bool = True) -> None:
        if home:
            self.home()
        await self.window.update(renderable)

    async def on_mount(self, event: events.Mount) -> None:
        assert isinstance(self.layout, GridLayout)
        self.layout.place(
            content=self.window,
            vscroll=self.vscroll,
            hscroll=self.hscroll,
        )
        await self.layout.mount_all(self)

    def home(self) -> None:
        self.x = self.y = 0

    def scroll_up(self) -> None:
        self.target_y += 1.5
        self.animate("y", self.target_y, easing="out_cubic", speed=80)

    def scroll_down(self) -> None:
        self.target_y -= 1.5
        self.animate("y", self.target_y, easing="out_cubic", speed=80)

    def page_up(self) -> None:
        self.target_y -= self.size.height
        self.animate("y", self.target_y, easing="out_cubic")

    def page_down(self) -> None:
        self.target_y += self.size.height
        self.animate("y", self.target_y, easing="out_cubic")

    def page_left(self) -> None:
        self.target_x -= self.size.width
        self.animate("x", self.target_x, speed=120, easing="out_cubic")

    def page_right(self) -> None:
        self.target_x += self.size.width
        self.animate("x", self.target_x, speed=120, easing="out_cubic")

    async def on_mouse_scroll_up(self, event: events.MouseScrollUp) -> None:
        self.scroll_up()

    async def on_mouse_scroll_down(self, event: events.MouseScrollUp) -> None:
        self.scroll_down()

    async def on_key(self, event: events.Key) -> None:
        await self.dispatch_key(event)

    async def key_down(self) -> None:
        self.target_y += 2
        self.animate("y", self.target_y, easing="linear", speed=100)

    async def key_up(self) -> None:
        self.target_y -= 2
        self.animate("y", self.target_y, easing="linear", speed=100)

    async def key_pagedown(self) -> None:
        self.target_y += self.size.height
        self.animate("y", self.target_y, easing="out_cubic")

    async def key_pageup(self) -> None:
        self.target_y -= self.size.height
        self.animate("y", self.target_y, easing="out_cubic")

    async def key_end(self) -> None:
        self.target_x = 0
        self.target_y = self.window.virtual_size.height - self.size.height
        self.animate("x", self.target_x, duration=1, easing="out_cubic")
        self.animate("y", self.target_y, duration=1, easing="out_cubic")

    async def key_home(self) -> None:
        self.target_x = 0
        self.target_y = 0
        self.animate("x", self.target_x, duration=1, easing="out_cubic")
        self.animate("y", self.target_y, duration=1, easing="out_cubic")

    async def message_scroll_up(self, message: Message) -> None:
        self.page_up()

    async def message_scroll_down(self, message: Message) -> None:
        self.page_down()

    async def message_scroll_left(self, message: Message) -> None:
        self.page_left()

    async def message_scroll_right(self, message: Message) -> None:
        self.page_right()

    async def message_scroll_to(self, message: ScrollTo) -> None:
        if message.x is not None:
            self.target_x = message.x
        if message.y is not None:
            self.target_y = message.y
        self.animate("x", self.target_x, speed=150, easing="out_cubic")
        self.animate("y", self.target_y, speed=150, easing="out_cubic")

    async def message_window_change(self, message: Message) -> None:
        virtual_size = self.window.virtual_size
        self.x = self.validate_x(self.x)
        self.y = self.validate_y(self.y)
        self.vscroll.virtual_size = virtual_size.height
        self.vscroll.window_size = self.size.height

        assert isinstance(self.layout, GridLayout)

        if self.layout.show_column("vscroll", virtual_size.height > self.size.height):
            self.refresh()
        if self.layout.show_row("hscroll", virtual_size.width > self.size.width):
            self.refresh()
