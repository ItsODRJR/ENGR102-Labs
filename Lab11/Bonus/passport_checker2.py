validCount = 0
validPassports = []

def isValid(passportFields):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "pid"]
    
    for field in requiredFields:
        if field not in passportFields:
            return False
    
    byr = passportFields["byr"]
    if not (byr.isdigit() and 1920 <= int(byr) <= 2007):
        return False

    iyr = passportFields["iyr"]
    if not (iyr.isdigit() and 2013 <= int(iyr) <= 2023):
        return False

    eyr = passportFields["eyr"]
    if not (eyr.isdigit() and 2023 <= int(eyr) <= 2033):
        return False

    hgt = passportFields["hgt"]
    if hgt.endswith("cm"):
        hgtValue = hgt[:-2]
        if not (hgtValue.isdigit() and 150 <= int(hgtValue) <= 193):
            return False
    elif hgt.endswith("in"):
        hgtValue = hgt[:-2]
        if not (hgtValue.isdigit() and 59 <= int(hgtValue) <= 76):
            return False
    else:
        return False

    hcl = passportFields["hcl"]
    if not (hcl.startswith("#") and len(hcl) == 7 and all(c in "0123456789abcdef" for c in hcl[1:])):
        return False

    pid = passportFields["pid"]
    if not (pid.isdigit() and len(pid) == 9):
        return False

    return True

while True:
    try:
        inputFilename = input("Enter the name of the file: ")

        with open(inputFilename, 'r') as inputFile:
            data = inputFile.read().strip().split("\n\n")
            break
    except:
        print("File not found, please try again.")

for passport in data:
    fields = {}
    for field in passport.replace("\n", " ").split(" "):
        key, value = field.split(":")
        fields[key] = value

    if isValid(fields):
        validCount += 1
        validPassports.append(passport)

with open("valid_passports2.txt", 'w') as outputFile:
    outputFile.write("\n\n".join(validPassports) + "\n")

print(f"There are {validCount} valid passports. Saved to valid_passports2.txt.")