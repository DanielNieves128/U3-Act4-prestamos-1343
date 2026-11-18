import pandas as pd
import matplotlib.pyplot as plt

# Daniel Nieves NC=1343

# 1. Crear diccionario con datos de préstamos aprobados
prestamos_aprobados = {
    'id_prestamo': [8001, 8002, 8003, 8004, 8005, 8006],
    'cliente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'tipo_prestamo': ['Personal', 'Hipotecario', 'Automotriz', 'Personal', 'Hipotecario', 'Estudiantil'],
    'monto_solicitado': [50000, 1500000, 300000, 30000, 2000000, 100000],
    'monto_aprobado': [50000, 1500000, 280000, 30000, 2000000, 100000],
    'plazo_meses': [24, 240, 60, 12, 300, 48],
    'tasa_interes_mensual': [2.5, 0.8, 1.2, 3.0, 0.8, 1.5],
    'pago_mensual_estimado': [2650, 13500, 6500, 2900, 18000, 2800],
    'fecha_desembolso': ['2024-01-10', '2023-06-15', '2023-11-20', '2024-01-05', '2022-08-01', '2023-09-10'],
    'estatus': ['Al corriente', 'Al corriente', 'Atrasado', 'Al corriente', 'Al corriente', 'Al corriente']
}

print("Analisis Exploratorio de Datos")
print("EDA, Exploratory Data Analysis Por Daniel Nieves NC=1343")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(prestamos_aprobados)

print("\n--- TABLA ORIGINAL DE PRESTAMOS ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+ Convertir el DataFrame en archivo CSV +-+-+")

df.to_csv(
    'prestamos_aprobados_1343.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nArchivo CSV creado correctamente")

print("+-+-+- 8. Leer los datos desde el archivo CSV -+-+-+")
print("prestamos_aprobados_1343.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('prestamos_aprobados_1343.csv')

print("\n--- DATOS LEIDOS DESDE CSV ---")
print(df)

print("+-+-+- 9. Analisis Exploratorio de Datos -+-+-+")

# 5. Primeros y ultimos registros
print("+-+-+- \n1. PRIMEROS REGISTROS (Head): -+-+-+")
print(df.head(3))  # Muestra los primeros 3

print("+-+-+- \n2. ULTIMOS REGISTROS (Tail): -+-+-+")
print(df.tail(2))  # Muestra los ultimos 2

# 6. Dimensiones y estructuras
print("+-+-+- 6. Dimensiones y estructuras -+-+-+")
print(df)

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)

print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)

print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACION GENERAL:")
df.info()

# 7. Estadisticas y limpieza
print("+*+*+*+ \n7. ESTADISTICAS DESCRIPTIVAS: -+-+-+")
print(df.describe())

print("+-+-+-\n8. VALORES FALTANTES (Nulls):-+-+-+")
print(df.isnull().sum())

print("+-+-+-\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES UNICOS POR COLUMNA:")
print(df.nunique())

print("Tipos de prestamos unicos:", df['tipo_prestamo'].unique())

# 8. Analisis especifico
print(df)
print("-------------------------------------------------------------------")

print("\n11. PRESTAMOS POR TIPO:")
print(df['tipo_prestamo'].value_counts())

print("\n12. PROMEDIO DE MONTO APROBADO: $", df['monto_aprobado'].mean())

print("13. MONTO APROBADO MAXIMO: $", df['monto_aprobado'].max())

print("14. MONTO APROBADO MINIMO: $", df['monto_aprobado'].min())

print("\nESTATUS DE LOS PRESTAMOS:")
print(df['estatus'].value_counts())

# 9. Ordenamiento, filtrado y agrupacion
print("9. Ordenamiento, filtrado y agrupacion")
print("-------------------------------------------------------------------")

print("+-+-+- \n15. PRESTAMOS ORDENADOS POR MONTO APROBADO (Mayor a menor):-+-+-+")

print(df.sort_values(by='monto_aprobado', ascending=False))

print("\n16. PRESTAMOS CON MONTO APROBADO MAYOR A $15,000:")

filtro = df[df['monto_aprobado'] > 15000]
print(filtro)

print("\n17. RESUMEN POR TIPO DE PRESTAMO:")

resumen = df.groupby('tipo_prestamo').agg(
    prestamos=('id_prestamo', 'count'),
    monto_promedio=('monto_aprobado', 'mean'),
    monto_maximo=('monto_aprobado', 'max')
)

print(resumen)

# 18. Grafica de barras: Prestamos por tipo
print("18. Grafica de barras: Prestamos por tipo")

conteo = df['tipo_prestamo'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Prestamos por tipo - Daniel 1343')
plt.xlabel('Tipo de prestamo')
plt.ylabel('Cantidad de prestamos')
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Grafica de barras: Montos aprobados por cliente
print("19. Grafica de barras: Montos aprobados por cliente")

plt.figure(figsize=(8, 5))
plt.bar(df['cliente'], df['monto_aprobado'], color='lightgreen')
plt.title('Monto aprobado por cliente - EDA Nieves 1343')
plt.xlabel('Cliente')
plt.ylabel('Monto aprobado en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribucion de plazos de prestamos
print("20. Histograma: Distribucion de plazos de prestamos")

plt.figure(figsize=(8, 5))
plt.hist(df['plazo_meses'], bins=5, color='orange', edgecolor='black')
plt.title('Distribucion de plazos de prestamos - Daniel 1343')
plt.xlabel('Plazo en meses')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Grafica de dispersion: Monto solicitado vs monto aprobado
print("21. Grafica de dispersion: Monto solicitado vs monto aprobado")

plt.figure(figsize=(8, 5))
plt.scatter(df['monto_solicitado'], df['monto_aprobado'], color='red', s=100)
plt.title('Relacion entre monto solicitado y aprobado - Daniel 1343')
plt.xlabel('Monto solicitado')
plt.ylabel('Monto aprobado')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribucion de montos aprobados
print("22. Diagrama de caja: Distribucion de montos aprobados")

plt.figure(figsize=(7, 5))
plt.boxplot(
    df['monto_aprobado'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue')
)
plt.title('Distribucion de montos aprobados (Boxplot) - Daniel 1343')
plt.ylabel('Monto aprobado en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlacion
correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACION ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()

plt.xticks(
    range(len(correlacion.columns)),
    correlacion.columns,
    rotation=45
)

plt.yticks(
    range(len(correlacion.columns)),
    correlacion.columns
)

plt.title('Matriz de correlacion de variables numericas EDA Daniel 1343')
plt.tight_layout()
plt.show()
print("Daniel Nieves NC = 1343")