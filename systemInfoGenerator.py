# Bruno Gaxiola Gonzalez A01253874
# Estudiante 3: Realiza un programa que genere una carpeta y dentro de la carpeta se deben generar 
# al menos 10 archivos txt con información del sistema. El programa debe de ser ejecutado en cualquier carpeta.

import os
import platform

# Generar la carpeta.
carpeta = "system_info"
os.makedirs(carpeta, exist_ok=True)

# Lista de funciones que proporcionan información del sistema.
funciones_info = [
    platform.system,
    platform.node,
    platform.version,
    lambda: str(platform.architecture()),  # Convertir tupla a cadena de texto
    platform.processor,
    platform.python_version,
    platform.platform,
    platform.machine,
    platform.release,
    lambda: str(platform.uname()) # Convertir tupla a cadena de texto
]

# Generar un archivo para cada función de información del sistema.
for i, funcion in enumerate(funciones_info):
    archivo = os.path.join(carpeta, f"system_info_{i}.txt")
    with open(archivo, "w") as f:
        f.write(funcion())

print("Archivos generados en la carpeta 'system_info'.")