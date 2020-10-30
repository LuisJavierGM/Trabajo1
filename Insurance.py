#%%
import numpy as np
import pandas as pd
#cuando importamos una librería y utilizamos "as" podemos abreviar la librería para facilitar cálculos.
lista=[1,2,4,6]
nplista= np.array(lista)
pdlista= pd.Series(lista)
print(lista*2)
print(nplista*2)
print(pdlista*2)

# %%
import pandas as pd
import numpy as np
#la tabla de trabajo de pandas es mejor conocida como data frame, por eso el nombre de la variable.
df= pd.read_csv("insurance-2.csv")
print(df)

# %%
import pandas as pd
import numpy as np
#la tabla de trabajo de pandas es mejor conocida como data frame, por eso el nombre de la variable.
df= pd.read_csv("insurance-2.csv")
df.head(10)
#variable.head(n) nos regresa los primeros n renglones del data frame.
df.tail(10)
#variable.tail(n) nos regresa los últimos n renglones del data frame.
df.sample(2)
#variable.sample(n) nos regresa n muestras aleatorias del data frame.

# %%
import pandas as pd
import numpy as np
#la tabla de trabajo de pandas es mejor conocida como data frame, por eso el nombre de la variable.
df= pd.read_csv("insurance-2.csv")
df.info()
#variable.info() muestra la información de los tipos de datos de nuestro data frame (int64,float64,object,date,etc).
df.describe()
#Muestra un resumen de estadística descriptiva (media, moda, mediana, cuartiles, desviación estandar, mínimo, máximo).

# %%
import pandas as pd
import numpy as np
df= pd.read_csv("insurance-2.csv")
#
df['age']
#
df[['age','bmi']]
df[2:4]
# %%
import pandas as pd
import numpy as np
df= pd.read_csv("insurance-2.csv")
#df[:2][['age']] para traer los primeros 2 renglones de age 
df[10:11][['age','bmi']]
df.iloc[[10]]
df.iloc[1:3]
# %%
#Medidas estadísticas 
import pandas as pd
import numpy as np
df= pd.read_csv("insurance-2.csv")
#Calcula medias de todas las variables.
df.mean()
#Calcula la media de 'age'
df['age'].mean()
#Calcula el primer cuartil de age 
df['age'].quantile(.25)
#calcula la moda de 'age' y 'bmi'
df[['age','bmi']].mode()
# %%
