maxTemp = float('-inf')
minTemp = float('inf')
totalAvgTemp = 0
totalHumidity = 0
totalWindSpeed = 0
precipitationDays = 0
daysCount = 0
monthNames = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

while True:
    try:
        monthName = input("Please enter a month: ").capitalize()
        month = monthNames.get(monthName)
        year = int(input("Please enter a year: "))
        if month is None:
            raise ValueError("Invalid month")
        break
    except:
        print("An error occurred. Please try again with the correct format (e.g., 'July' and '2022').")

with open("WeatherData.csv") as file:
    headers = file.readline().strip().split(',')
    for line in file:
        fields = line.strip().split(',')
        
        date = fields[0]
        try:
            avgWindSpeed = float(fields[1]) if fields[1] else None
            precipitation = float(fields[2]) if fields[2] else None
            avgHumidity  = float(fields[3]) if fields[3] else None
            avgTemp = float(fields[4]) if fields[4] else None
            maxTemperature = float(fields[5]) if fields[5] else None
            minTemperature = float(fields[6]) if fields[6] else 0
        except:
            print(f"Invalid data line: {line}")
            continue

        dateParts = date.split('/')
        dateMonth = int(dateParts[0])
        dateYear = int(dateParts[2])

        if dateMonth == month and dateYear == year:
            if maxTemperature is not None:
                maxTemp = max(maxTemp, maxTemperature)
            if minTemperature is not None:
                minTemp = min(minTemp, minTemperature)
            if avgTemp is not None:
                totalAvgTemp += avgTemp
            if avgHumidity is not None:
                totalHumidity += avgHumidity
            if avgWindSpeed is not None:
                totalWindSpeed += avgWindSpeed
            if precipitation > 0:
                precipitationDays += 1
            daysCount += 1

print(f"10-year maximum temperature: {maxTemp} F")
print(f"10-year minimum temperature: {minTemp} F")

if daysCount > 0:
    print(f"\nFor {monthName} {year}:")
    print(f"Mean average daily temperature: {totalAvgTemp / daysCount:.1f} F")
    print(f"Mean relative humidity: {totalHumidity / daysCount:.1f}%")
    print(f"Mean daily wind speed: {totalWindSpeed / daysCount:.2f} mph")
    print(f"Percentage of days with precipitation: {precipitationDays / daysCount * 100:.1f}%")
else:
    print("No data available for the specified month and year.")