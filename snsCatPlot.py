# -- BASIC CATPLOT --
import seaborn as sns

df = sns.load_dataset('mpg')
sns.catplot(data=df, x="cylinders", y="displacement");


# -- CATPLOT WITH SPECIFIED 'col' PARAMETER -- 
import seaborn as sns
df = sns.load_dataset('mpg')

sns.catplot(data=df, x="cylinders", y="displacement", col = 'origin');


# -- CATPLOT WITH SPECIFIED 'col' and 'hue' PARAMETERS -- 
import seaborn as sns
df = sns.load_dataset('mpg')

sns.catplot(data=df, x="cylinders", y="displacement", col = 'origin', hue = 'model_year');


# -- CATPLOT WITH SPECIFIED 'col', 'hue', and 'kind' PARAMETERS -- 
import seaborn as sns
df = sns.load_dataset('mpg')

sns.catplot(data=df, x="cylinders", y="displacement", col = 'origin', hue = 'model_year', kind = 'box');
