import sys

TOKENS_POR_MILLON = 1_000_000 
DIAS_POR_MES = 30

MODELOS = {             
            "rapido": {"entrada": 0.25, "salida": 1.25},
            "medio": {"entrada": 3.00, "salida": 15.00},
            "grande": {"entrada": 15.00, "salida": 75.00},
                }


def calcular_costo(modelo, tokens_entrada, tokens_salida):
    precio_entrada = MODELOS[modelo]["entrada"]
    precio_salida = MODELOS[modelo]["salida"]
    costo_entrada = tokens_entrada / TOKENS_POR_MILLON * precio_entrada
    costo_salida = tokens_salida / TOKENS_POR_MILLON * precio_salida
    total = costo_entrada + costo_salida
    return total     


modelo = input("Modelo (rapido/medio/grande): ").strip().lower()
if modelo not in MODELOS:
    sys.exit(f"Error: Modelo no existe. Disponibles: {', '.join(MODELOS)}")
try:
    tokens_entrada = int(input("Tokens de entrada por peticion: "))
    tokens_salida = int(input("Tokens de salida por peticion: "))
    peticiones_dia = int(input("Peticiones por dia: "))
except ValueError:
    sys.exit("Error: La cantidad debe ser un numero entero")
if tokens_entrada < 0 or tokens_salida < 0 or peticiones_dia < 0:
    sys.exit("Error: Los valores no pueden ser negativos")
costo_peticion = calcular_costo(modelo, tokens_entrada, tokens_salida)
costo_diario = costo_peticion * peticiones_dia
costo_mensual = costo_diario * DIAS_POR_MES
print(f"Costo por peticion: ${costo_peticion:.4f}")
print(f"Costo diario: ${costo_diario:.4f}")
print(f"Costo mensual: ${costo_mensual:.4f}")
