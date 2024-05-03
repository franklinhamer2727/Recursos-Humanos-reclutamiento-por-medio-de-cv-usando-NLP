import matplotlib.pyplot as plt
from busqueda_similitud import procesar
datos = procesar()


# Extraer los nombres y las sumas de habilidades y experiencia de cada persona
nombres = [nombre for persona in datos for nombre in persona.keys()]
suma_habilidades = [persona['count_habilidades'] for persona in datos for nombre, persona in persona.items()]
suma_experiencia = [persona['count_experiencia'] for persona in datos for nombre, persona in persona.items()]

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
barWidth = 0.35
r1 = range(len(nombres))
r2 = [x + barWidth for x in r1]

plt.bar(r1, suma_habilidades, color='skyblue', width=barWidth, edgecolor='grey', label='Suma de Habilidades')
plt.bar(r2, suma_experiencia, color='salmon', width=barWidth, edgecolor='grey', label='Suma de Experiencia')

plt.xlabel('Personas')
plt.ylabel('Suma')
plt.xticks([r + barWidth/2 for r in range(len(nombres))], nombres, rotation=45)
plt.legend()
plt.title('Suma de Habilidades y Experiencia por Persona')

# Agregar etiquetas en las barras
for i, (habilidad, experiencia) in enumerate(zip(suma_habilidades, suma_experiencia)):
    plt.text(i, habilidad + 0.1, habilidad, ha='center', va='bottom', color='black')
    plt.text(i + barWidth, experiencia + 0.1, experiencia, ha='center', va='bottom', color='black')

plt.tight_layout()

# Mostrar el gráfico
plt.show()
