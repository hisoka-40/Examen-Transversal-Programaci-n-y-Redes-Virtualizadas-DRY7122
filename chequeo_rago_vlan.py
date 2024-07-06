# verificar_vlan.py

def verificar_rango_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1000:
        print(f"La VLAN {numero_vlan} pertenece al rango normal.")
    elif 1002 <= numero_vlan <= 4094:
        print(f"La VLAN {numero_vlan} pertenece al rango extendido.")
    else:
        print(f"El número de VLAN {numero_vlan} no es válido.")

if __name__ == "__main__":
    try:
        vlan = int(input("Ingrese el número de VLAN: "))
        verificar_rango_vlan(vlan)
    except ValueError:
        print("Error: Debe ingresar un número entero para la VLAN.")
