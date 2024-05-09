import os
import zipfile
import sys

def desencriptar_archivos(zip_path, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destino)
        print("Archivos desencriptados y extraídos exitosamente.")

    os.remove(zip_path)
    print("Archivo ZIP original eliminado.")

def main():
    if len(sys.argv) < 3:
        print("Uso: python desencriptar_archivos.py <ruta_del_zip> <destino>")
        sys.exit(1)

    zip_path = sys.argv[1]
    destino = sys.argv[2]

    desencriptar_archivos(zip_path, destino)

if __name__ == "__main__":
    main()
