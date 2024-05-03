import matplotlib.pyplot as plt
from busqueda_similitud import procesar
datos = procesar()

# Extraer los nombres y los conteos de habilidades y experiencia de cada persona
nombres = [nombre for persona in datos for nombre in persona.keys()]
conteos_habilidades = [persona['count_habilidades'] for persona in datos for nombre, persona in persona.items()]
conteos_experiencia = [persona['count_experiencia'] for persona in datos for nombre, persona in persona.items()]

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
barWidth = 0.35
r1 = range(len(nombres))
r2 = [x + barWidth for x in r1]

plt.bar(r1, conteos_habilidades, color='skyblue', width=barWidth, edgecolor='grey', label='Habilidades')
plt.bar(r2, conteos_experiencia, color='salmon', width=barWidth, edgecolor='grey', label='Experiencia')

plt.xlabel('Personas')
plt.ylabel('Conteo')
plt.xticks([r + barWidth/2 for r in range(len(nombres))], nombres, rotation=45)
plt.legend()
plt.title('Conteo de Habilidades y Experiencia por Persona')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
