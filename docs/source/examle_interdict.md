```py
       """
       Created on Tue Nov  2 09:20:04 2021

       Illustration avec un exemple de couplages à éviter

       @author: HEDI
       """

       import WaterOptim.wpinch as wp

       # Définition de l'inventaire
       usages=[{'name':'process 1','cin_max':0,'cout_max':100,'mc':2},
              {'name':'process 2','cin_max':50,'cout_max':100,'mc':5},
              {'name':'process 3','cin_max':50,'cout_max':800,'mc':30},
              {'name':'process 4','cin_max':400,'cout_max':800,'mc':4,}]    

       """     
       définition des couplages à éviter:
           process 2 -> process 4 : Interdiction
           process 1 -> process 3 : Interdiction
       """
       interdictions = [("process 2","process 4"),
                        ("process 1","process 3")]   

       r= wp.__pinch__(usages=usages,verbose=1, interdictions=interdictions)

```
