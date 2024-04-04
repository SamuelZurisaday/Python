paises_campeones_del_mundo = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "Espana",
    2014: "Alemania",
    2018: "Francia",
    2022: "Argentina"
}

print(
    f"Los paises campeones del mundo FIFA desde 1990 al 2022, son: {paises_campeones_del_mundo}")
print()

ano_de_copa = input("Introduzca el anio para saber el equipo Campeon: ")
ano_de_copa = int(ano_de_copa)

campeon_del_ano = paises_campeones_del_mundo.get(
    ano_de_copa, "Valor no encontrado")
print()

print(
    f"En el anio {ano_de_copa} fue campeon de la Copa Mundial: {campeon_del_ano}")