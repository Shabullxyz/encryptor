#import os
import sys
import argparse
from cryptography.fernet import Fernet

def generar_clave(keyfile):
    """
    Función que genera una clave y la guarda en un archivo.
    """
    clave = Fernet.generate_key()
    with open(keyfile, "wb") as f:
        f.write(clave)

def encriptar(archivo, keyfile):
    """
    Función que encripta un archivo usando una clave.
    """
    with open(archivo, "rb") as f:
        contenido = f.read()
    with open(keyfile, "rb") as f:
        clave = f.read()
    fernet = Fernet(clave)
    contenido_encriptado = fernet.encrypt(contenido)
    with open(archivo + ".enc", "wb") as f:
        f.write(contenido_encriptado)

def desencriptar(archivo_enc, keyfile):
    """
    Función que desencripta un archivo usando una clave.
    """
    with open(archivo_enc, "rb") as f:
        contenido_encriptado = f.read()
    with open(keyfile, "rb") as f:
        clave = f.read()
    fernet = Fernet(clave)
    contenido_desencriptado = fernet.decrypt(contenido_encriptado)
    with open(archivo_enc[:-4], "wb") as f:
        f.write(contenido_desencriptado)

def main():
    """
    Función principal del programa.
    """
    parser = argparse.ArgumentParser(description="Encriptador")
    parser.add_argument("archivo", help="Archivo a encriptar o desencriptar")
    parser.add_argument("-g", "--generar-clave", action="store_true", help="Generar una nueva clave y guardarla en un archivo")
    parser.add_argument("-k", "--keyfile", default=".encriptador.key", help="Archivo donde se guarda/lee la clave (por defecto: .encriptador.key)")
    parser.add_argument("-d", "--desencriptar", action="store_true", help="Desencriptar el archivo en vez de encriptarlo")
    args = parser.parse_args()

    # Generar una nueva clave y salir
    if args.generar_clave:
        generar_clave(args.keyfile)
        print("Clave generada correctamente.")
        sys.exit()

    # Encriptar o desencriptar el archivo
    if args.desencriptar:
        desencriptar(args.archivo, args.keyfile)
        print("Archivo desencriptado correctamente.")
    else:
        encriptar(args.archivo, args.keyfile)
        print("Archivo encriptado correctamente.")

if __name__ == "__main__":
    main()
