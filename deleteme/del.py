import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Crear datos de ejemplo
np.random.seed(42)
data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D', 'E'],
    'Valores': np.random.randint(30, 100, 5),
    'Valores2': np.random.randint(20, 90, 5)
})

# Configuración general de estilo
plt.style.use('seaborn')
sns.set_palette("husl")

# 1. Gráfico de barras moderno
plt.figure(figsize=(12, 6))

# Gráfico principal
ax = plt.subplot(121)
bars = plt.bar(data['Categoría'], data['Valores'])

# Personalización
plt.title('Gráfico de Barras Moderno', pad=20, fontsize=14)
plt.xlabel('Categorías', labelpad=10)
plt.ylabel('Valores', labelpad=10)

# Añadir valores sobre las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom')

# Estilo minimalista
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 2. Gráfico de barras con gradiente
ax2 = plt.subplot(122)
# Crear gradiente
colors = plt.cm.viridis(np.linspace(0, 0.8, len(data)))
bars2 = plt.bar(data['Categoría'], data['Valores2'], color=colors)

# Personalización
plt.title('Gráfico de Barras con Gradiente', pad=20, fontsize=14)
plt.xlabel('Categorías', labelpad=10)
plt.ylabel('Valores', labelpad=10)

# Añadir valores sobre las barras
for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom')

# Estilo minimalista
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# 3. Gráfico de barras horizontales con estilo seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=data, y='Categoría', x='Valores', 
            palette='rocket')
plt.title('Gráfico de Barras Horizontal con Seaborn', pad=20)
plt.xlabel('Valores', labelpad=10)
plt.ylabel('Categorías', labelpad=10)
plt.show()

# 4. Gráfico de barras apiladas
plt.figure(figsize=(10, 6))
bottom = np.zeros(len(data))

# Primera capa de barras
plt.bar(data['Categoría'], data['Valores'], label='Serie 1',
        alpha=0.7)

# Segunda capa de barras
plt.bar(data['Categoría'], data['Valores2'], bottom=data['Valores'],
        label='Serie 2', alpha=0.7)

plt.title('Gráfico de Barras Apiladas', pad=20)
plt.xlabel('Categorías', labelpad=10)
plt.ylabel('Valores', labelpad=10)
plt.legend()

# Estilo minimalista
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()
