file = open("values.txt", "a+")

while(True):
    print("Enter name of alcohol")
    AlcoholName = input()
    if(AlcoholName == "quit"):
        break
    AlcoholVolume = input("Enter volume (ml)")
    AlcoholPercentage = input("Enter percentage (%)")
    AlcoholPrice = input("Enter price (£)")
    AlcoholValue = (AlcoholVolume*AlcoholPercentage)/AlcoholPrice
    file.write(AlcoholName + ", " + AlcoholValue)

file.close()
