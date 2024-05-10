from histoire import get_moyenne_histoire
from mathematiques import get_moyenne_mathematiques

def calcul_moyenne():
    moyenne_histoire = get_moyenne_histoire()
    moyenne_mathematiques = get_moyenne_mathematiques()
    moyenne_totale = (moyenne_histoire + moyenne_mathematiques) / 2
    return moyenne_totale

if __name__ == "__main__":
    moyenne = calcul_moyenne()
    print("La moyenne totale de l'étudiant est :", moyenne)
