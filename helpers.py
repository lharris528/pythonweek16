import random as r


genders = ["Male", "Female"]

femaleNames = ["Bella", "Luna", "Lucy", "Daisy", "Lola",
               "Sadie", "Molly", "Bailey", "Stella", "Maggie",
               "Chloe", "Penny", "Nala", "Zoey", "Lily",
               "Coco", "Sophie", "Rosie", "Ellie", "Ruby",
               "Piper", "Mia", "Roxy", "Gracie", "Millie"]

maleNames = ["Max", "Charlie", "Cooper", "Buddy", "Milo",
             "Bear", "Rocky", "Duke", "Tucker", "Jack",
             "Oliver", "Teddy", "Leo", "Bentley", "Zeus",
             "Jax", "Toby", "Winston", "Ollie", "Louie",
             "Finn", "Murphy", "Moose", "Loki", "Gus"]

lastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones",
             "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
             "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
             "Thomas", "Taylor", "Moore", "Jackson", "Martin",
             "Lee", "Perez", "Thompson", "White", "Harris",
             "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
             "Walker", "Young", "Allen", "King", "Wright",
             "Scott", "Torres", "Nguyen", "Hill", "Flores",
             "Green", "Adams", "Nelson", "Baker", "Hall",
             "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"]

breeds = ["Border Collie", "Labrador Retriever", "Greyhound", "Beagle", "Shiba Inu",
          "Golden Retriever", "English Bulldog", "Pug", "Alaskan Malamute", "Shih Tzu",
          "West Highland Terrier", "Borzoi", "Mastiff", "Akita", "Boxer"]

colors = ["black", "white", "brown", "red", "yellow", "gold", "cream", "gray", "blue"]

medicalConditions = ["Cancer", "Diabetes", "Heartworm", "Kennel Cough",
                     "Parvovirus", "Rabies", "Ringworm", "Broken Leg",
                     "Ear Infection", "Skin Infection", "Dental Disease", "Vomiting/Diarrhea",
                     "Stiffness/Pain", "Urinary Problems", "Obesity", "Severe Bites/Scratches",
                     "Fleas", "Canine Coronavirus", "Lyme Disease", "Blastomycosis",
                     "Coccidioidomycosis", "Giardiasis", "Protothecosis", "Hookworms",
                     "Tapeworms", "Whipworms", "Congestive heart failure", "Osteoarthritis",
                     "Congenital Vertebral Anomalies", "Back Pain", "Hemolytic Anemia", "Mites",
                     "Pericardial Effusion", "Epilepsy", "Cataracts", "Pancreatitis"]


def getGender():
        index = r.randint(0, 1)
        gender = genders[index]
        return gender


def getFirstName(gender):
    index = r.randint(0, 24)
    if gender == "Male":
        firstName = maleNames[index]
    elif gender == "Female":
        firstName = femaleNames[index]
    return firstName


def getLastName():
    index = r.randint(0, 49)
    lastName = lastNames[index]
    return lastName


def getWeight():
    weight = r.randint(5, 250)
    return weight


def getBreed():
    index = r.randint(0, 14)
    breed = breeds[index]
    return breed


def getAge():
    age = r.randint(1, 23)
    return age


def getColor():
    numColors = r.randint(0, 3)
    route = colors
    if numColors < 2:
        index = r.randint(0, 8)
        color = colors[index]
    elif numColors == 2:
        indices = getRandNoDuplicateIndices(0, 8, 2)
        color = f"{route[indices[0]]} and {route[indices[1]]}"
    elif numColors == 3:
        indices = getRandNoDuplicateIndices(0, 8, 3)
        color = f"{route[indices[0]]}, {route[indices[1]]}, and {route[indices[2]]}"
    return color


def getMedicalCondition():
    numConditions = r.randint(0, 6)
    route = medicalConditions
    if numConditions < 3:
        index = r.randint(0, 35)
        medicalCondition = route[index]
    elif numConditions < 5:
        indices = getRandNoDuplicateIndices(0, 35, 2)
        medicalCondition = f"{route[indices[0]]} and {route[indices[1]]}"
    elif numConditions == 5:
        indices = getRandNoDuplicateIndices(0, 35, 3)
        medicalCondition = f"{route[indices[0]]}, {route[indices[1]]}, and {route[indices[2]]}"
    elif numConditions == 6:
        nums = getRandNoDuplicateIndices(0, 35, 4)
        medicalCondition = f"{route[nums[0]]}, {route[nums[1]]}, {route[nums[2]]}, and {route[nums[3]]}"
    return medicalCondition


def getRandNoDuplicateIndices(start, end, numberOfIndices):
    indexArray = []
    indexSet = set()
    i = 0
    while i < numberOfIndices:
        newIndex = r.randint(start, end)
        indexArray.append(newIndex)
        indexSet.add(newIndex)
        if len(indexSet) != len(indexArray):
            indexArray.remove(newIndex)
            continue
        i += 1
    return indexArray
