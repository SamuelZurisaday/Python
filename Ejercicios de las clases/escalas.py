# Definición del círculo de quintas
circulo_quintas = ['C', 'G', 'D', 'A', 'E',
                   'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']

# Definición de las firmas de clave: cantidad de sostenidos o bemoles
# Mayor
firmas_clave_mayor = {
    'C': 0, 'G': 1, 'D': 2, 'A': 3, 'E': 4, 'B': 5, 'F#': 6, 'Db': -5, 'Ab': -4, 'Eb': -3, 'Bb': -2, 'F': -1
}

# Menor (relativo menor de cada mayor basado en el círculo de quintas)
firmas_clave_menor = {
    'A': 0, 'E': 1, 'B': 2, 'F#': 3, 'C#': 4, 'G#': 5, 'D#': 6, 'Bb': -5, 'F': -4, 'C': -3, 'G': -2, 'D': -1
}


def encontrar_escala(nota, es_mayor=True):
    if es_mayor:
        firmas_clave = firmas_clave_mayor
    else:
        firmas_clave = firmas_clave_menor

    cantidad_firmas = firmas_clave.get(nota)

    if cantidad_firmas is not None:
        if cantidad_firmas > 0:
            print(
                f"La escala de {nota} {'mayor' if es_mayor else 'menor'} tiene {cantidad_firmas} sostenido(s).")
        elif cantidad_firmas < 0:
            print(
                f"La escala de {nota} {'mayor' if es_mayor else 'menor'} tiene {abs(cantidad_firmas)} bemol(es).")
        else:
            print(
                f"La escala de {nota} {'mayor' if es_mayor else 'menor'} no tiene alteraciones.")
    else:
        print("Nota no encontrada en el círculo de quintas.")


# Ejemplo de uso
nota_raiz = input("Ingrese la nota raíz (ejemplo: C, G, D, etc.): ")
encontrar_escala(nota_raiz, es_mayor=True)  # Para la escala mayor
encontrar_escala(nota_raiz, es_mayor=False)  # Para la escala menor