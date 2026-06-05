# analisis_ventas.py
# Rodrigo Zampa - TP Organización Empresarial UTN 2026
# Análisis básico de ventas simuladas

import pandas as pd
import matplotlib.pyplot as plt

# cargo el csv desde la carpeta datos
datos = pd.read_csv("datos/ventas.csv")

# agrego una columna con el total de cada venta
datos["total"] = datos["cantidad"] * datos["precio"]

# cuanto se vendió en total
total_general = datos["total"].sum()
print(f"Total vendido: ${total_general:,.2f}")

# qué producto se vendió más (por cantidad)
mas_vendido = datos.groupby("producto")["cantidad"].sum().idxmax()
print(f"El producto más vendido fue: {mas_vendido}")

# ventas agrupadas por mes
datos["fecha"] = pd.to_datetime(datos["fecha"])
datos["mes"] = datos["fecha"].dt.month
por_mes = datos.groupby("mes")["total"].sum()
print("\nVentas por mes:")
print(por_mes)

# armo el gráfico
plt.figure(figsize=(8, 5))
por_mes.plot(kind="bar", color="steelblue")
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total ($)")
plt.xticks(ticks=[0,1,2], labels=["Enero","Febrero","Marzo"], rotation=0)
plt.tight_layout()

# guardo el gráfico en resultados
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado ok")
