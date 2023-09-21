import random


winNum = []
  
def lottoziehung(aufrufe, rafflenumbers):
    i = 44 - aufrufe
    index = random.randint(0,i) 
    
   
    choosenNumbers = rafflenumbers[index]
    rafflenumbers[index] = rafflenumbers[i]
    rafflenumbers[i] = choosenNumbers
    winNum.append(choosenNumbers)
 
 
rafflenumbers = [] 
for x in range(45):
    rafflenumbers.append(x+1)  
        
for i in range(6):
    lottoziehung(i, rafflenumbers)
    
print(winNum)