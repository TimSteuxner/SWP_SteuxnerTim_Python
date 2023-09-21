import random

def lottoziehung():
    numbers = list(range(1, 46))
   
    alreadyChosen = []

    while len(alreadyChosen) <= 5:
        
        rndNumb = random.choice(numbers)

        if rndNumb not in alreadyChosen:
           alreadyChosen.append(rndNumb)

    print("Lottozahlen lauten:", alreadyChosen)


lottoziehung()