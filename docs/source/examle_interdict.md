```py
       # -*- coding: utf-8 -*-
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

Pour afficher le réseau d'eau :

```py
       >> r.design.draw()
```

![Réseau 1](https://github.com/ROMDHANA/WaterOptim/blob/main/docs/source/interdict1.svg)

Si on interdit tous les couplages avec le poste 2 :

```py
     interdictions = [
                      ("process 2","process 1")
                      ("process 2","process 3"),
                      ("process 2","process 4")]  
```

Résultat montre un message en rouge au niveau du poste 4 qui présente un déficit :


![Réseau 2](https://github.com/ROMDHANA/WaterOptim/blob/main/docs/source/interdict2.svg)


