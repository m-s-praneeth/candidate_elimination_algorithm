import pandas as pd
import numpy as np
data = pd.read_csv("enjoysport.csv")
concepts = np.array(data.iloc[:,:-1])
target = np.array(data.iloc[:,-1])
print(concepts)
print()
print(target)
print()
def learn(concepts,target):
    print("Initializing specific and general hypothesis")
    print()
    specific_h = concepts[0].copy()
    general_h = [['?'for i in range(len(specific_h))]for i in range(len(specific_h))]
    print(specific_h)
    print()
    print(general_h)
    print()
    for i,b in enumerate(concepts):
        print("for loop starts")
        print()
        if target[i]=='yes':
            print("for positive instance")
            print()
            for x in range(len(specific_h)):
                if b[x]!=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
        if target[i]=='no':
            print("for negative instance")
            print()
            for x in range(len(specific_h)):
                if b[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
        print('step number',i+1,"of candidate elimination algorithm")
        print(specific_h)
        print()
        print(general_h)
        print()
    indices = [i for i,val in enumerate(general_h) if val==['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
s_hyp,g_hyp = learn(concepts,target)
print("final specific hypothesis is: ",s_hyp)
print("final general hypothesis is: ",g_hyp)
