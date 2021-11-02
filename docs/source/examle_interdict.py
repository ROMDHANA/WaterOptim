import WaterOptim.wpinch as wp

usages=[{'name':'process 1','cin_max':0,'cout_max':100,'mc':2},
       {'name':'process 2','cin_max':50,'cout_max':100,'mc':5,'loc':"A"},
       {'name':'process 3','cin_max':50,'cout_max':800,'mc':30,'loc':'B'},
       {'name':'process 4','cin_max':400,'cout_max':800,'mc':4,'loc':"B"}]    

#Dominic Foo
sources=[{'name':'Distillation bottoms','c':0,'m':.8*3600/1000},
              {'name':'Off-gas condensate','c':14,'m':5*3600/1000},
              {'name':'Aqueous layer','c':25,'m':5.9*3600/1000},
              {'name':'Ejector condensate','c':34,'m':1.4*3600/1000}]
demands = [{'name':'BFW0','cin_max':0,'m':1.2*3600/1000},
                {'name':'BFW','cin_max':10,'m':5.8*3600/1000},
                {'name':'BFW1','cin_max':1,'m':19.8*3600/1000}]

inter=[("Distillation bottoms",'BFW'),("Off-gas condensate","BFW1")]
   
r1=wp.__pinch__(sinks=demands,sources=sources,verbose=True, interdictions=inter)        

interdictions = [("process 2","process 4"),("process 2","process 3")]        
r= wp.__pinch__(usages=usages,verbose=1, interdictions=interdictions)
