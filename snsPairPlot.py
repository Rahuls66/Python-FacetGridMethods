# -- BASIC PAIRPLOT --
import seaborn as sns
df = sns.load_dataset('penguins')

sns.pairplot(df, dropna = True);


# -- PAIRPLOT WITH SPECIFIED 'hue' PARAMETER --
import seaborn as sns
df = sns.load_dataset('penguins')

sns.pairplot(df, dropna = True, hue = 'island');


# -- PAIPLOT WITH SPECIFIED 'hue' AND 'kind' PARAMETERS --
import seaborn as sns
df = sns.load_dataset('penguins')

sns.pairplot(df, dropna = True, hue = 'island', kind = 'kde');
