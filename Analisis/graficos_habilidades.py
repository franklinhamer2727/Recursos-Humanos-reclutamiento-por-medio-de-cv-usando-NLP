import matplotlib.pyplot as plt
from busqueda_similitud import procesar
datos = procesar()

# Extraer los nombres y los conteos de habilidades de cada persona
nombres = [nombre for persona in datos for nombre in persona.keys()]
conteos_habilidades = [persona['count_habilidades'] for persona in datos for nombre, persona in persona.items()]


# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(nombres, conteos_habilidades, color='skyblue')
plt.xlabel('Personas')
plt.ylabel('Conteo de Habilidades')
plt.title('Conteo de Habilidades por Persona')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
