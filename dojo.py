from helpers import (getGender, getFirstName, getLastName, getWeight, getBreed, getAge, getColor, getMedicalCondition)


class dojo:

    companyName = "Doge's Dojo of Healing"

    companyMotto = '"For Doges, by Doges"'

    patientList = []

    def __init__(self, gender, firstName, lastName, weight, breed, age, color, medicalCondition):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.weight = weight
        self.breed = breed
        self.age = age
        self.color = color
        self.medicalCondition = medicalCondition

    def addRandomPatient(self):
        gender = getGender()
        dog = dojo(
            gender,
            getFirstName(gender),
            getLastName(),
            getWeight(),
            getBreed(),
            getAge(),
            getColor(),
            getMedicalCondition()
        )
        return dog

    def addRandomPatients(self, number):
        i = 0
        while i < int(number):
            dog = self.addRandomPatient(dojo)
            self.patientList.append(dog)
            i += 1

    def addOnePatient(self):
        dog = dojo(
            input("Gender: "),
            input("First Name: "),
            input("Last Name: "),
            input("Weight (in pounds): "),
            input("Breed: "),
            input("Age: "),
            input("Color: "),
            input("Medical Condition: ")
        )
        self.patientList.append(dog)
        input("Thank you for putting your dog in our care!\nPress Enter When Ready")

    def printPatientList(self):
        print(
          f"{self.companyName}\n"
          f"{self.companyMotto}"
        )
        for i, dog in enumerate(self.patientList):
            print(
                f"{i + 1}. {dog.firstName} {dog.lastName}"
            )

    def printPatientDetails(self, number):
        number = int(number) - 1
        dog = self.patientList[number]
        print(
            f"Gender: {dog.gender}\n"
            f"First name: {dog.firstName}\n"
            f"Last name: {dog.lastName}\n"
            f"Weight: {dog.weight} lbs.\n"
            f"Breed: {dog.breed}\n"
            f"Age: {dog.age} years old\n"
            f"Color: {dog.color}\n"
            f"Medical Condition(s): {dog.medicalCondition}"
        )

    def navigateDojo(self):
        self.printPatientList(dojo)
        response = input(
            "Select an option by typing its corresponding number into the terminal.\n"
            "List of options:\n"
            "1. See Patient Details \n"
            "2. Fill Out New Patient Form\n"
            "3. Add Random Patient(s)\n"
            "4. Remove a Patient\n"
            "5. Exit Program\n"
        )
        if response == "1":
            response2 = input("Type the number of the dog you would like you to see more information about.\n")
            self.printPatientDetails(dojo, response2)
            input("Press Enter When Done Viewing Details")
            self.navigateDojo(dojo)
        elif response == "2":
            self.addOnePatient(dojo)
            self.navigateDojo(dojo)
        elif response == "3":
            self.addRandomPatients(dojo, input("How many new patients would you like to add?\n"))
            self.navigateDojo(dojo)
        elif response == "4":
            index = input("Enter the number of the patient you would like to remove.\n")
            index = int(index) - 1
            self.patientList.pop(index)
            self.navigateDojo(dojo)
        else:
            return

# Uncomment the next line to have the Dojo start with 5 patients, or
# simply add them yourself once you run navigateDojo.
# dojo.addRandomPatients(dojo, 5)
dojo.navigateDojo(dojo)
