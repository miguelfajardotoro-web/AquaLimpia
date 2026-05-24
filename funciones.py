import pandas as pd

def cargar_datos(ruta):
    """
    Carga un archivo Excel y devuelve un DataFrame.
    
    Parámetros:
    ruta (str): Ruta del archivo Excel a cargar.
    
    Retorna:
    pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_excel(ruta)
        print("Datos cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# CALCULAR EFICIENCIA DBO

def calcular_eficiencia_DBO(df):
    """
    Calcula la eficiencia de DBO y la agrega al DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene las columnas 'DBO_inicial' y 'DBO_final'.
    
    Retorna:
    pd.DataFrame: DataFrame con una nueva columna 'eficiencia_DBO'.
    """
    df = df.copy()
    df["eficiencia_DBO"] = (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"]) / df["DBO_entrada_mg_L"] * 100
    return df

# Cumplimiento por planta
def clasificar_cumplimiento_planta(df):
    cumplimiento  = df.groupby(
        'planta'
    )['cumplimiento_norma'].mean() * 100
    return cumplimiento

# CALCULAR CUMPLIMIENTO
def calcular_cumplimiento_planta(valor_dbo):
    if valor_dbo <= 30:
        return "Cumple"
    else:   
        return "No Cumple"
    
# VALIDAR VALORES NULOS
def validar_valores_nulos(df):
    nulos = df.isnull().sum()
    print("Valores nulos por columna:")
    print(nulos)

# VALIDAR DUPLICADOS
def validar_duplicados(df):
    duplicados = df.duplicated().sum()
    print(f"Cantidad de filas duplicadas: {duplicados}")



def cargar_datos(ruta):
    return pd.read_excel(ruta)