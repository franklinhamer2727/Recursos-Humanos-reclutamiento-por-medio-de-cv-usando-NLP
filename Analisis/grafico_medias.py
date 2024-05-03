import matplotlib.pyplot as plt
from busqueda_similitud import procesar
datos = procesar()


# Extraer los nombres y las sumas de habilidades y experiencia de cada persona
nombres = [nombre for persona in datos for nombre in persona.keys()]
suma_habilidades = [persona['count_habilidades'] for persona in datos for nombre, persona in persona.items()]
suma_experiencia = [persona['count_experiencia'] for persona in datos for nombre, persona in persona.items()]

# Calcular las medias de habilidades y experiencia
media_habilidades = sum(suma_habilidades) / len(suma_habilidades)
media_experiencia = sum(suma_experiencia) / len(suma_experiencia)

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

# Agregar etiquetas de media
plt.axhline(y=media_habilidades, color='blue', linestyle='--', label=f'Media de Habilidades: {media_habilidades:.2f}')
plt.axhline(y=media_experiencia, color='red', linestyle='--', label=f'Media de Experiencia: {media_experiencia:.2f}')

# Mostrar el gráfico
plt.tight_layout()
plt.legend()
plt.show()