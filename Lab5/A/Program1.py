def calculate_risk(age, sex, total_chol, hdl, sbp, smoker, treated):
    sex = sex.upper()
    smoker = smoker.upper()

    # Age points
    if sex == "M":
        if 20 <= age <= 34:
            age_points = -9
        elif 35 <= age <= 39:
            age_points = -4
        elif 40 <= age <= 44:
            age_points = 0
        elif 45 <= age <= 49:
            age_points = 3
        elif 50 <= age <= 54:
            age_points = 6
        elif 55 <= age <= 59:
            age_points = 8
        elif 60 <= age <= 64:
            age_points = 10
        elif 65 <= age <= 69:
            age_points = 11
        elif 70 <= age <= 74:
            age_points = 12
        elif 75 <= age <= 79:
            age_points = 13
        else:
            return "Invalid age"
    elif sex == "F":
        if 20 <= age <= 34:
            age_points = -7
        elif 35 <= age <= 39:
            age_points = -3
        elif 40 <= age <= 44:
            age_points = 0
        elif 45 <= age <= 49:
            age_points = 3
        elif 50 <= age <= 54:
            age_points = 6
        elif 55 <= age <= 59:
            age_points = 8
        elif 60 <= age <= 64:
            age_points = 10
        elif 65 <= age <= 69:
            age_points = 12
        elif 70 <= age <= 74:
            age_points = 14
        elif 75 <= age <= 79:
            age_points = 16
        else:
            return "Invalid age"

    # Cholesterol points
    if sex == "M":
        if total_chol >= 280:
            if 20 <= age <= 39:
                chol_points = 11
            elif 40 <= age <= 49:
                chol_points = 8
            elif 50 <= age <= 59:
                chol_points = 5
            elif 60 <= age <= 69:
                chol_points = 3
            elif 70 <= age <= 79:
                chol_points = 1
        elif total_chol >= 240:
            if 20 <= age <= 39:
                chol_points = 9
            elif 40 <= age <= 49:
                chol_points = 6
            elif 50 <= age <= 59:
                chol_points = 4
            elif 60 <= age <= 69:
                chol_points = 2
            elif 70 <= age <= 79:
                chol_points = 1
        elif total_chol >= 200:
            if 20 <= age <= 39:
                chol_points = 7
            elif 40 <= age <= 49:
                chol_points = 5
            elif 50 <= age <= 59:
                chol_points = 3
            elif 60 <= age <= 69:
                chol_points = 1
            elif 70 <= age <= 79:
                chol_points = 0
        elif total_chol >= 160:
            if 20 <= age <= 39:
                chol_points = 4
            elif 40 <= age <= 49:
                chol_points = 3
            elif 50 <= age <= 59:
                chol_points = 2
            elif 60 <= age <= 69:
                chol_points = 1
            elif 70 <= age <= 79:
                chol_points = 0
        else:
            chol_points = 0
    elif sex == "F":
        if total_chol >= 280:
            if 20 <= age <= 39:
                chol_points = 13
            elif 40 <= age <= 49:
                chol_points = 10
            elif 50 <= age <= 59:
                chol_points = 7
            elif 60 <= age <= 69:
                chol_points = 4
            elif 70 <= age <= 79:
                chol_points = 2
        elif total_chol >= 240:
            if 20 <= age <= 39:
                chol_points = 11
            elif 40 <= age <= 49:
                chol_points = 8
            elif 50 <= age <= 59:
                chol_points = 5
            elif 60 <= age <= 69:
                chol_points = 3
            elif 70 <= age <= 79:
                chol_points = 2
        elif total_chol >= 200:
            if 20 <= age <= 39:
                chol_points = 8
            elif 40 <= age <= 49:
                chol_points = 6
            elif 50 <= age <= 59:
                chol_points = 4
            elif 60 <= age <= 69:
                chol_points = 2
            elif 70 <= age <= 79:
                chol_points = 1
        elif total_chol >= 160:
            if 20 <= age <= 39:
                chol_points = 4
            elif 40 <= age <= 49:
                chol_points = 3
            elif 50 <= age <= 59:
                chol_points = 2
            elif 60 <= age <= 69:
                chol_points = 1
            elif 70 <= age <= 79:
                chol_points = 1
        else:
            chol_points = 0

    # HDL points
    if hdl >= 60:
        hdl_points = -1
    elif 50 <= hdl <= 59:
        hdl_points = 0
    elif 40 <= hdl <= 49:
        hdl_points = 1
    else:
        hdl_points = 2

    # Systolic BP points
    if sex == "M":
        if sbp >= 160:
            sbp_points = 3 if treated else 2
        elif sbp >= 140:
            sbp_points = 2 if treated else 1
        elif sbp >= 130:
            sbp_points = 2 if treated else 1
        elif sbp >= 120:
            sbp_points = 1 if treated else 0
        else:
            sbp_points = 0
    elif sex == "F":
        if sbp >= 160:
            sbp_points = 6 if treated else 4
        elif sbp >= 140:
            sbp_points = 5 if treated else 3
        elif sbp >= 130:
            sbp_points = 4 if treated else 2
        elif sbp >= 120:
            sbp_points = 3 if treated else 1
        else:
            sbp_points = 0

    # Smoking points
    if sex == "M":
        if 20 <= age <= 39:
            smoker_points = 8 if smoker == "Y" else 0
        elif 40 <= age <= 49:
            smoker_points = 5 if smoker == "Y" else 0
        elif 50 <= age <= 59:
            smoker_points = 3 if smoker == "Y" else 0
        elif 60 <= age <= 69:
            smoker_points = 1 if smoker == "Y" else 0
        elif 70 <= age <= 79:
            smoker_points = 1 if smoker == "Y" else 0
        else:
            return "Invalid age"
    elif sex == "F":
        if 20 <= age <= 39:
            smoker_points = 9 if smoker == "Y" else 0
        elif 40 <= age <= 49:
            smoker_points = 7 if smoker == "Y" else 0
        elif 50 <= age <= 59:
            smoker_points = 4 if smoker == "Y" else 0
        elif 60 <= age <= 69:
            smoker_points = 2 if smoker == "Y" else 0
        elif 70 <= age <= 79:
            smoker_points = 1 if smoker == "Y" else 0
        else:
            return "Invalid age"

    # Total points
    total_points = age_points + chol_points + hdl_points + sbp_points + smoker_points


    # Risk estimation 
    if sex == "M":
        if total_points < 0:
            return "<1%"
        elif total_points <= 4:
            return "1%"
        elif total_points == 5:
            return "2%"
        elif total_points == 6:
            return "2%"
        elif total_points == 7:
            return "3%"
        elif total_points == 8:
            return "4%"
        elif total_points == 9:
            return "5%"
        elif total_points == 10:
            return "6%"
        elif total_points == 11:
            return "8%"
        elif total_points == 12:
            return "10%"
        elif total_points == 13:
            return "12%"
        elif total_points == 14:
            return "16%"
        elif total_points == 15:
            return "20%"
        elif total_points == 16:
            return "25%"
        elif total_points >= 17:
            return "30% or more"
    elif sex == "F":
        if total_points < 9:
            return "<1%"
        elif total_points == 9:
            return "1%"
        elif total_points == 10:
            return "1%"
        elif total_points == 11:
            return "1%"
        elif total_points == 12:
            return "2%"
        elif total_points == 13:
            return "2%"
        elif total_points == 14:
            return "3%"
        elif total_points == 15:
            return "4%"
        elif total_points == 16:
            return "5%"
        elif total_points == 17:
            return "6%"
        elif total_points == 18:
            return "8%"
        elif total_points == 19:
            return "11%"
        elif total_points == 20:
            return "14%"
        elif total_points == 21:
            return "17%"
        elif total_points == 22:
            return "22%"
        elif total_points == 23:
            return "27%"
        elif total_points >= 24:
            return "30% or more"

sex = input("Enter sex (M/F): ")
age = int(input("Enter age: "))
total_chol = int(input("Enter total cholesterol level: "))
hdl = int(input("Enter HDL cholesterol level: "))
sbp = int(input("Enter systolic blood pressure (SBP): "))
smoker = input("Smoker? (Y/N): ")
treated = input("Blood pressure treated? (Y/N): ")

total_10_year_risk = calculate_risk(age, sex, total_chol, hdl, sbp, smoker, treated.upper() == "Y")
print(f"Estimated 10-year risk: {total_10_year_risk}")