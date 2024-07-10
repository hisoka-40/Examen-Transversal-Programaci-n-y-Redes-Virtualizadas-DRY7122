import hashlib

def obtener_hash(texto):
    """Función para obtener el hash SHA-256 de un texto."""
    return hashlib.sha256(texto.encode()).hexdigest()

def almacenar_usuario_contrasena():
    """Función para ingresar usuarios y contraseñas y almacenarlas en hash."""
    usuarios = {}
    
    while True:
        usuario = input("Ingrese el nombre de usuario (o 'fin' para terminar): ").strip()
        
        if usuario.lower() == 'fin':
            break
        
        contrasena = input("Ingrese la contraseña: ").strip()
        
        # Guardar en hash
        hash_contrasena = obtener_hash(contrasena)
        usuarios[usuario] = hash_contrasena
        
        print(f"Usuario '{usuario}' almacenado con contraseña en hash: {hash_contrasena}")
    
    return usuarios

def main():
    print("Bienvenido al programa de almacenamiento de usuarios y contraseñas en hash.")
    usuarios = almacenar_usuario_contrasena()
    print("\nUsuarios almacenados:")
    for usuario, hash_contrasena in usuarios.items():
        print(f"Usuario: {usuario}, Hash de contraseña: {hash_contrasena}")

if __name__ == "__main__":
    main()
