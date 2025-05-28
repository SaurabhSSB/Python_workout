country_population= {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}
f= "Yes"
while f== "Yes":
    work = input("Enter Operation( print/ add/ remove/ query): ")
    if work== "print":
        print(country_population)
    elif work== "add":
        country_1= input("Enter country name:- ")
        if country_1 in country_population:
            print("Country name already exists.")
        else:
            population_1= int(input("Enter country population:- "))
            country_population[country_1]= population_1
    elif work== "remove":
        country_removal= input("Enter the name of the country to be removed:- ")
        if country_removal in country_population:
            del country_population[country_removal]
            print(f"{country_removal} data removed successfully")
        else:
            print("Country name does not exist in the dictionary.")
    else:
        country_2= input("Enter the name of the country:- ")
        if country_2 in country_population:
            print( country_population[country_2])
        else:
            print("Country name does not exist in the dictionary.")
    f= input("Do you wish to continue( Yes/ No):")
print(country_population)