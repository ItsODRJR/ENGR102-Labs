# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: OSCAR RODRIGUEZ (635007029)
# THANG CHAU (335000995)
# NATHANIEL ALVARENGA (735000064)
# JONATHAN BOZONE (835005736)
# Section: ENGR-102-551
# Assignment: Lab11A
# Date: 30/10/24

validCount = 0
validPassports = []

def isVaild(passportFields):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "pid"]
    for field in requiredFields:
        if field not in passportFields:
            return False
    return True

while True:
    try:
        inputFilename = input("Enter the name of the file: ")
        outputFilename = "valid_passports.txt"

        with open(inputFilename, 'r') as inputFile: # using with it closes the file automatically afterwards
            data = inputFile.read().strip().split("\n\n")
            break
    except:
        print("File not found, please try again.")

for passport in data:
    fields = {}
    for field in passport.replace("\n", " ").split(" "):
        key, value = field.split(":")
        fields[key] = value

    
    if isVaild(fields):
        validCount += 1
        validPassports.append(passport)

with open(outputFilename, 'w') as outputFile:
    outputFile.write("\n\n".join(validPassports) + "\n")

print(f"There are {validCount} valid passports")