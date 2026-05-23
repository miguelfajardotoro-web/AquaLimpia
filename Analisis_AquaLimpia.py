import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear directorio para gráficos si no existe
os.makedirs("graficos", exist_ok=True)
os.makedirs("reportes", exist_ok=True)

# Cargar dataset
df = pd.read_excel("dataset_set_A_aguas_residuales.xlsx")

# Visualizar primeras filas
print(df.head())
print(df.info())

# Convertir fecha
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
# Calcular eficiencia DBO
df['eficienia_dbo'] = (
    (df['DBO_entrada_mg_L'] - df['DBO_salida_mg_L'])
    / df['DBO_entrada_mg_L']
) * 100
# Estadísticas descriptivas
print(df.describe())
# Cumplimiento por planta
cumplimiento = df.groupby('planta')[
    'cumplimiento_norma'
].mean() * 100

print(cumplimiento)

# Gráfico DBO salida
plt.figure(figsize=(10,6))

sns.boxplot(
    x='planta',
    y='DBO_salida_mg_L',
    data=df
)

plt.title('DBO salida por planta')
plt.xticks(rotation=45)

# Guardar gráfico
plt.savefig("graficos/dbo_salida_por_planta.png")
plt.show()

# Correlación
plt.figure(figsize=(10,8))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='Blues'
)

plt.title('Mapa de correlación')
# Guardar gráfico
plt.savefig( "graficos/mapa_correlacion.png")
plt.show()

# Exportar archivo operaciones
operaciones = df[['fecha_registro','planta','caudal_entrada_m3_d','DBO_entrada_mg_L',
    'DBO_salida_mg_L','energia_aeracion_kWh','lodos_generados_kg_d','eficienia_dbo'
]]

operaciones.to_csv('reportes/operaciones.csv', index=False)
# Exportar archivo ambiental
ambiental = df[['fecha_registro', 'planta','DBO_salida_mg_L','cumplimiento_norma']]

ambiental.to_csv('reportes/gestion_ambiental.csv', index=False)
print("Archivos exportados correctamente")
