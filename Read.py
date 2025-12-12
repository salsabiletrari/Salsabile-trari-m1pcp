#trarisalsabilM1pcp
#trari salsabil m1 pcp le 11/12/2025
#Meftah mayssane
#benmoussa siham
#HiouliSarah
#tekia sanae

import pandas as pd

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
  "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGT", "TTAACCGGAT"],
  "Longueur": [12, 12, 12, 10, 11, 10, 10], 
  "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]   } 
} 

#1) Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("**************** Creation et affichage *****************")

# Affichage du tableau
print("Tableau des séquences ADN :", "\n" "\n")
print(df, "\n" "\n")

# Opérations sur les tableaux:
print("************** Operations ***************")

#2) Sélectionner la colonne "Longueur"
Longueur = df["Longueur"]
print(Longueur, "\n" "\n")

#3)Filtrer les séquences avec Longueur supérieur à 10
print("************* Filtrage avec la Longueur *************")
# Filtrer les séquences avec Longueur supérieur à 10
filtered_df = df[df["Longueur"] > 10]
print(filtered_df, "\n" "\n")
