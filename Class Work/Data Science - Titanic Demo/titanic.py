import csv

with open("Class Work/Data Science - Titanic Demo/titanic.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    femaleSuvivors = 0
    teenSurvivors = 0
    for row in reader:
        if row[1] == '1' and row[4] == 'female':
            femaleSuvivors += 1

        if row[1] == '1' and row[5] < '18':
            teenSurvivors += 1
    
    print(f"Number of female survivors: {femaleSuvivors}")
    print(f"Number of teen survivors: {teenSurvivors}")