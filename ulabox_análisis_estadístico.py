#%%
import pandas as pd
df= pd.read_csv("ulabox.csv")
#df.tail()
#df.info()
df.describe()

# %%
import pandas as pd
df= pd.read_csv("ulabox.csv")
df.tail()

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("ulabox.csv")
df.info()
#BOXPLOT DISCOUNT
sns.set_theme(style="white")
df.boxplot(by ="weekday",grid='True',column =['discount%'], color='red')

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("ulabox.csv")
df.info()

sns.set_theme(style="white")
sns.histplot(x="weekday",y="total_items",data=df)

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("ulabox.csv")
sns.heatmap(df.corr())

# %%
import pandas as pd
import seaborn as sns
df= pd.read_csv("ulabox.csv")
g = sns.histplot(data=df, x="hour", multiple="stack", hue="weekday")
for q in df.hour.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
