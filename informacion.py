nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
altura = float(input("¿Cuál es tu altura en metros? "))
eres_estudiante = input("¿Eres estudiante? (Si/No) ").strip().lower() == "si"
color_favorito = input("¿Cuál es tu color favorito? ")
numero_de_la_suerte = int(input("¿Cuál es tu número de la suerte? "))
horas_que_duermes_en_la_noche = int(input("¿Cuántas horas duermes por las noches? "))
te_gusta_la_programación = input("¿Te gusta la programación? (Si/No) ").strip().lower() == "si"

print("\n--- Resumen de Respuestas ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Eres estudiante?", "Sí" if eres_estudiante else "No")
print("Color favorito:", color_favorito)
print("Número de la suerte:", numero_de_la_suerte)
print("Horas de sueño:", horas_que_duermes_en_la_noche)
print("¿Te gusta la programación?", "Sí" if te_gusta_la_programación else "No")