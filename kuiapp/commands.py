import re
import subprocess

def get_namespaces() -> list:
    # Ejecutar comando de kubernetes para sacar el texto
    # Guardar el resultado en un array 

    #ejecutas el comando y obtienes el resultado en utf-8
    namespaces = subprocess.run(["kubectl", "get", "ns", "--no-headers", "-o", "custom-columns=:metadata.name"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    ns = namespaces.split("\n")
    ns = list(filter(None, ns))
    return ns


def get_pods(contenedor: str) -> str:
    pods = subprocess.run(["kubectl", "get", "pods", "-n", contenedor], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    return pods    

def get_pods_names(contenedor: str) -> str:
    names = subprocess.run(["kubectl", "get", "pods", "-n", contenedor, "--no-headers", "-o", "custom-columns=:metadata.name"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    names = names.split("\n")
    names = list(filter(None, names))
    return names