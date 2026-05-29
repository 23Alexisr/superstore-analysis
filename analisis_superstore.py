
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# convierte el archivo csv en un dataframe para poder trabajar con los datos limpiarlos, filtrarlos
df= pd.read_csv("Superstore.csv" , encoding="latin1")
# Elimina duplicados para evitar sesgo en el análisis nuestro Data Frame
df=df.drop_duplicates()
#elimina los registros nulos de nuesto Data Frame
df= df.dropna()
#Retorna los primeros dos regristos de nuestro Data Frame
print (df.head(2))
# nos muestra ubn resumen detallado de la estrcutura de nuestro Data Frame
print (df.info())
# muestra un resumen estadistico de las columnas numericas del nuestro Data Frame
print(df.describe())

#Muestra la ventas totales agrupadas por categoria
print("*************************")
print (" Ventas por categoria ")
print("*************************")
print(df.groupby("Category")["Sales"].sum() .reset_index())

#Muestra la ventas totales agrupadas por Region
print("*************************")
print (" Ventas por Region ")
print("*************************")
print(df.groupby("Region")["Sales"].sum() .reset_index())

# Visualiza el top 5 de las sub-categorias mas rentables 
print("*************************")
print (" Top 5 Sub-Categorias con mayor venta ")
print("*************************")
rent = df.groupby("Sub-Category")["Sales"].sum() .reset_index()
rent = rent.sort_values("Sales", ascending=False)
rent = rent.head(5)
print(rent)

# Visualiza las 5 Sub-categorias con menos ventas
print("*************************")
print (" 5 Sub-Categorias con menos venta ")
print("*************************")
rent = df.groupby("Sub-Category")["Sales"].sum() .reset_index()
rent = rent.sort_values("Sales")
rent = rent.head(5)
print(rent)

# visulaiza las ganancias por cada segmento de nuestro Data Frame
print("*************************")
print (" Ganancia por Segmento ")
print("*************************")
profi= df.groupby("Segment")["Profit"].sum() .reset_index()
profi= profi.sort_values("Profit", ascending=False)
print (profi)
# Agrega un nueva columna de margen de ganancia en porcentaje %
df["Margen"]=(df["Profit"]/df["Sales"])*100
print (df)

#agraga un nueva columan de sobre clasificar el producto si es rentable o no 

def clasifica (Profit):
    if Profit > 0 :
        return "Rentable"
    else :
        return "No Rentable"

df["Clasificación"]= df["Profit"].apply(clasifica)

print (df)
 
 # muestra las ventas totales por sub categoria en un grafico de barras de seaborn, tambien se puede observar en el grafico de mayor a menor 
rent = df.groupby("Sub-Category")["Sales"].sum() .reset_index()
rent = rent.sort_values("Sales" , ascending=False)
sns.barplot( rent, x="Sub-Category", y="Sales")
plt.title("Ventas Totales por Sub-Categoria")
plt.show()

 # muestra el total de descuentos por categoria
descuentos = df.groupby("Category")["Discount"] .sum() .reset_index()
sns.barplot(descuentos, x="Category", y="Discount" )
plt.title("Total de descuentos por Categoria")
plt.show()

# muestra el total de Ventas Por Region
porcen = df.groupby("Region")["Sales"] .sum() .reset_index()
sns.lineplot(porcen , x="Region",y="Sales")
plt.title("Total de ventas por Region")
plt.show()