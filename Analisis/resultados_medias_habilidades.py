import matplotlib.pyplot as plt
from busqueda_similitud import procesar
datos = procesar()

for persona in datos[0].values():
    habilidades = persona.get('habilidades', [])
    experiencia = persona.get('experiencia', [])

    suma_habilidades = sum([hab[0] for hab in habilidades])
    media_habilidades = suma_habilidades / len(habilidades) if len(habilidades) > 0 else 0

    suma_experiencia = sum([exp[0] for exp in experiencia])
    media_experiencia = suma_experiencia / len(experiencia) if len(experiencia) > 0 else 0

    print(f"Persona: {persona}")
    print(f"Suma de habilidades: {suma_habilidades}")
    print(f"Media de habilidades: {media_habilidades}")
    print(f"Suma de experiencia: {suma_experiencia}")
    print(f"Media de experiencia: {media_experiencia}")
    print("-" * 50)


# Datos proporcionados
nombres = []
suma_habilidades = []
media_habilidades = []
suma_experiencia = []
media_experiencia = []
nombres = [nombre for persona in datos for nombre in persona.keys()]
for persona in datos[0].values():

    habilidades = persona.get('habilidades', [])
    experiencia = persona.get('experiencia', [])

    suma_habilidades.append(sum([hab[0] for hab in habilidades]))
    media_habilidades.append(sum([hab[0] for hab in habilidades]) / len(habilidades) if len(habilidades) > 0 else 0)

    suma_experiencia.append(sum([exp[0] for exp in experiencia]))
    media_experiencia.append(sum([exp[0] for exp in experiencia]) / len(experiencia) if len(experiencia) > 0 else 0)

# Crear el gráfico de barras mejorado
plt.figure(figsize=(12, 8))

barWidth = 0.2
r1 = range(len(nombres))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth * 2 for x in r1]

colors_habilidades = ['#1f77b4', '#aec7e8'] * len(nombres)
colors_experiencia = ['#ff7f0e', '#ffbb78'] * len(nombres)

plt.bar(r1, suma_habilidades, color=colors_habilidades, width=barWidth, edgecolor='grey', label='Habilidades')
plt.bar(r2, media_habilidades, color=colors_habilidades, width=barWidth, edgecolor='grey')
plt.bar(r3, suma_experiencia, color=colors_experiencia, width=barWidth, edgecolor='grey', label='Experiencia')
plt.bar(r3, media_experiencia, color=colors_experiencia, width=barWidth, edgecolor='grey')

# Agregar etiquetas a las barras con los valores numéricos
for i, (hab_suma, hab_media, exp_suma, exp_media) in enumerate(zip(suma_habilidades, media_habilidades, suma_experiencia, media_experiencia)):
    plt.text(i - 0.2, hab_suma + 0.1, f"{hab_suma:.2f}", ha='center', va='bottom', color='black')
    plt.text(i, hab_media + 0.1, f"{hab_media:.2f}", ha='center', va='bottom', color='black')
    plt.text(i + 0.2, exp_suma + 0.1, f"{exp_suma:.2f}", ha='center', va='bottom', color='black')
    plt.text(i + 0.4, exp_media + 0.1, f"{exp_media:.2f}", ha='center', va='bottom', color='black')

# Agregar etiquetas a cada barra con el nombre del valor
for i, nombre in enumerate(nombres):
    plt.text(i - 0.2, suma_habilidades[i] + 0.3, nombre, ha='center', va='bottom', color='black', rotation=90)
    plt.text(i, media_habilidades[i] + 0.3, nombre, ha='center', va='bottom', color='black', rotation=90)
    plt.text(i + 0.2, suma_experiencia[i] + 0.3, nombre, ha='center', va='bottom', color='black', rotation=90)
    plt.text(i + 0.4, media_experiencia[i] + 0.3, nombre, ha='center', va='bottom', color='black', rotation=90)

plt.xlabel('Personas')
plt.ylabel('Valor')
plt.title('Comparación de Suma y Media de Habilidades y Experiencia por Persona')
plt.legend()
plt.xticks([r + barWidth for r in range(len(nombres))], nombres, rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()