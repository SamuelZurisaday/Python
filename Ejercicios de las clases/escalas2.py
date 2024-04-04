# Notas en la escala cromática para generar escalas
notas_cromaticas = ['C', 'C#', 'D', 'D#',
                    'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Intervalos para generar escalas mayores y menores
intervalos_mayor = [2, 2, 1, 2, 2, 2, 1]  # T-T-ST-T-T-T-ST
intervalos_menor = [2, 1, 2, 2, 1, 2, 2]  # T-ST-T-T-ST-T-T

# Función para generar una escala basada en la nota raíz y los intervalos


def generar_escala(nota_raiz, intervalos):
    escala = [nota_raiz]
    indice_nota = notas_cromaticas.index(nota_raiz)
    for intervalo in intervalos:
        indice_nota = (indice_nota + intervalo) % 12
        escala.append(notas_cromaticas[indice_nota])
    return escala

# Función para encontrar la relativa menor/mayor


def encontrar_relativa(nota_raiz, es_mayor=True):
    if es_mayor:
        escala = generar_escala(nota_raiz, intervalos_mayor)
        # La relativa menor está en la sexta posición de la escala mayor
        relativa = escala[5]
    else:
        escala = generar_escala(nota_raiz, intervalos_menor)
        # La relativa mayor se encuentra subiendo tres semitonos (o bajando 9) desde la menor
        indice_relativa = (notas_cromaticas.index(nota_raiz) + 9) % 12
        relativa = notas_cromaticas[indice_relativa]
    return relativa

# Función principal para mostrar la escala y su relativa


def mostrar_escala_y_relativa(nota_raiz, es_mayor=True):
    if es_mayor:
        escala = generar_escala(nota_raiz, intervalos_mayor)
        tipo = "mayor"
    else:
        escala = generar_escala(nota_raiz, intervalos_menor)
        tipo = "menor"

    relativa = encontrar_relativa(nota_raiz, es_mayor)
    tipo_relativa = "menor" if es_mayor else "mayor"

    print(f"La escala de {nota_raiz} {tipo} es: {' - '.join(escala)}")
    print(f"Su escala relativa {tipo_relativa} es: {relativa}")


# Ejemplo de uso
nota_raiz = input(
    "Ingrese la nota raíz (ejemplo: C, G, D, etc.): ").capitalize()
es_mayor = input("Es esta una escala mayor? (s/n): ").lower() == 's'
mostrar_escala_y_relativa(nota_raiz, es_mayor)
