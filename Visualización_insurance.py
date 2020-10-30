#%%
import pandas as pd
import seaborn as sns
df= pd.read_csv("insurance-2.csv")
df.info()
#Investigar set_theme style
sns.set_theme(style="white")
#Diagrama de Barras
sns.displot(x="region",data=df)
sns.displot(x="bmi",data=df)
sns.displot(x="region",hue="sex",multiple="stack",data=df)
#Cuando analizamos una variable de muchas columnas seaborn automaticamente nos genera un histograma pero podemos ponerlo directamente como histplot.
sns.displot(x="age",data=df)

#%%
import pandas as pd
import seaborn as sns
df= pd.read_csv("insurance-2.csv")
sns.set_theme(style="white")

g=sns.histplot(x="age",multiple="stack",hue="sex",data=df)
for q in df.age.quantile([.25,.5,.75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("insurance-2.csv")
sns.set_theme(style="white")
#Calcular el coeficiente de correlación de Pearson
df.corr()
#Para visualizar mejor la Tabla de correlación podemos usar un Heatmap
sns.heatmap(df.corr(),annot=True)
#Podemos ver, sin embargo, que no existe una correlación lineal aparente entre pares de variables. Para corroborar esto, les propongo que construyamos un diagrama de dispersión (también llamado "scatterplot").
sns.scatterplot(data=df,x="age",y="charges")
sns.scatterplot(data=df,x="bmi",y="charges",hue="smoker")

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("insurance-2.csv")
sns.set_theme(style="white")

#Categorización de variables numéricas

pd.cut(df.age,[17,20,35,50,64],labels=['Adolecente','Joven adulto','Adulto','Adulto Mayor'])

#Como se puede observar, el comando anterior nos permitió asignar a cada observación una categoria
#  dependiendo del intervalo de edad al que pertenece el beneficiario del seguro. Lo que vamos a 
# hacer ahora es agregar esa categoría como una columna adicional a nuestro dataset.
#  Para eso, ejecutemos la siguiente celda:

df['edad_cat']=pd.cut(df.age,[17,20,35,50,64],labels=['Adolecente','Joven Adulto','Adulto','Adulto Mayor'])

#Como edad_cat aparece ya como otra variable en el dataset, es posible usarla directamente en la creación de diagramas.
sns.scatterplot(data=df,x="edad_cat",y="charges")

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("insurance-2.csv")
sns.set_theme(style="white")
#Transformación de variables categóricas en numéricas
#Aunque parezca extraño, en ocasiones tendremos necesidad de transformar una variable categórica en numérica. 
# En nuestro ejemplo, este tipo de transformación será útil para agregar las variables categóricas en el cálculo 
# de el coeficiente de correlación y su correspondiente heapmap. Para ilustrar el proceso, transformemos la variable
#  sex en nuestro dataset. Para eso, ejecute la siguiente celda:
df['sex_num']=df.sex.astype('category')
df['sex_num']