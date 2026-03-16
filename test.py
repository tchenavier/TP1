# Mini test : graphique seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("donner.csv")

print ("moddule importer avec succes")
# Mini test : graphique seaborn



sns.boxplot(x="Danger", y="vitesse", data=df) 
plt.title("Exemple graphique : vitesse selon danger") 
plt.show() 
