integrantes = [
    ("Diego", "Soto"),
    ("Nicolas", "Gonzalez"),
]

def imprimir_lista(integrantes):
    if integrantes:
        print("Lista de Integrantes:")
        for nombre, apellido in integrantes:
            print(f"{nombre} {apellido}")
    else:
        print("No hay integrantes para mostrar.")
        
imprimir_lista(integrantes)
