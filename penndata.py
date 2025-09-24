import pandas as pd
import random

fNames = ["Mac", "Danielle""", "Aiden", "Ben", "Van", "Kaden", "Lucian", "Andrew", "Benedict", "Keaton", "Joe", "Noah", "Roman", "Kyan", "Elijah", "Alexis", "Katerina", "Jill", "Jane", "Emmy", "Emma", "Rachel", "Eliana", "Marge", "Lisa"]
lNames = ["Bill"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Victory Lap"]
pathways = ["Business", "Marketing", "Construction"]
names = []

for i in range(20000):
    names.append(f"{random.choice[fNames]}) {random.choice[lNames]}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names ],
    "GPA": [round(random.uniform(0.3, 4.0),2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)

print(pennData)