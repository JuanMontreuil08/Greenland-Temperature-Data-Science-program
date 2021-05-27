
#Import csv library
import csv

#Constants, List with each month of a year as elements
CONSTANT_MONTHS = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
    ]

#Main function
def main():

    #Welcome to the program
    print("Welcome to the program")
    print(
        "Today we are going to see quick facts about Greenland¨s temperature and the impact on Atlantic sea levels"
        )
    print("")



    #While true, continue ask the user for what he/she is looking for
    #until que press enter to finish 
    while True:
        print("")
        print(">>Information available: <<")
        print("PRESS 0 FOR: FINISHING THE PROGRAM")
        print("PRESS 1 FOR: Greenland¨s Temperature per month [Data available: 1991-2020]")
        print("PRESS 2 FOR: Greenland¨s Rainfall per month [Data available: 1991-2020]")
        print("PRESS 3 FOR: Comparing Atlantic sea level tendency for two given years [Data available: 1993-2020]")
        print("")
        user_request = input("Choose what info do you need: ")
        
        #if statements, posible outputs represented from 1-4
        #If press 1, apply the first function
        if user_request == "1":

            #Ask the user for a year to consult (convert to int to meet type)
            given_year = int(input("Provide a year from [1991-2020] to get the registered Temperatures: "))

            #Function call de temperature per month
            #return list with all the temperatures of a given year
            my_list = temp_per_month(given_year)

            #Loop over each value of that year and print them
            for i in range(len(my_list)):
                print("Temperature in",CONSTANT_MONTHS[i],"was", my_list[i])
            
            #We show the maximun temperature and minimun on that given year
            max_temperature = max(my_list)
            min_temperature = min(my_list)

            print("Highest Temperature on",given_year, "was", max_temperature )
            print("Lowest Temperature on",given_year, "was", min_temperature )
        
        #if press 2, apply this..
        elif user_request == "2":
            given_year2 = int(input("Provide a year from [1991-2020] to get the registered Rainfall mm: "))
            my_list2 = rainfall_per_month(given_year2)

            #Variable store the average Rainfall value on the year
            average_year = sum(my_list2) / len(my_list2)

            for i in range(len(my_list2)):
                #print the rainfall registered on each month in the given year
                print("Rainfall mm", "in",CONSTANT_MONTHS[i], "was", my_list2[i])
            
            print("")
            print("Average Rainfall mm was",average_year)
            print("")
            
            #2second for loop, return on which months the rainfall was higher than average 
            #in given year
            for i in range(len(my_list2)):
                if my_list2[i] > average_year:
                    print("On month", CONSTANT_MONTHS[i], "Rainfall was higher than average")
                else:
                    pass
        
        #If user press 3
        elif user_request == "3":
            #ask user for the two years to compare
            First= int(input("Provide year 1: "))
            Second = int(input("Provide year 2: "))
            print("")
            #calling the function
            atlantic_Sea(First,Second)
        
        #if user press 0, finish the program
        elif user_request == "0":
            print("CLOSING THE PROGRAM...")
            break

#Helper functions
def temp_per_month(year):

    #Empty list
    temp_range = []

    #Read each line of the csv file as lists
    with open("Temperature.csv") as f:

        #Avoid the first line (columns)
        next(f)
        reader = csv.reader(f)

        #for each recorrer cada línea
        for line in reader:

            #Evaluate if the element at index 1 (years ) is the one that
            #we are consulting
            if int((line[1])) == year:

                #We add to our new list all the temperatures in that specific
                #year
                temp_range.append(float(line[0]))
            
            #Else, just pass the other lines
            else:
                pass

    #return the list with all the temperatures per month in that given year
    return temp_range

#Similar function to Temperature but here the user get the registered rainfall (mm)
def rainfall_per_month(year):

    #Empty list
    rainfall_range =[]

    with open("RainFall.csv") as f:
        next(f)
        reader = csv.reader(f)

        for line in reader:

            if int(line[1]) == year:
                #append the rainfall mm on each month in that given year
                rainfall_range.append(float(line[0]))
            
            else:
                pass
    
    return rainfall_range

#function return the tendency of atlantic sea level in a given year vs year 2
def atlantic_Sea(year1, year2):

    #FIRST PART_ BUILDING THE LIST
    #Empty list will contain the sea level mm on that given year 1
    values1 = []
    #Empty list will contain the sea level mm on that given year 2
    values2 = []

    #read the csv file, each line as a list
    with open("Atlantic_Sea_Levels.csv") as f:
        reader = csv.reader(f)
        #recorremos cada línea
        for line in reader:
            #Store the string version of line[0] element (year)
            string_year = str(line[0])
            #evalue if the element[0] starts with given year 1 (we want that data)
            if string_year.startswith(str(year1)) :
                #variable will store the value
                each_value1 = 0
                #add to list, the values of sea mm
                while each_value1 == 0:
                    #will go through each possible values and take one (SEA LEVEL MM)
                    #on each line list at given year
                    for i in range(1,len(line)):
                        if line[i] == "":
                            pass
                        else:
                            #add value at our list
                            each_value1 = line[i]
                            values1.append(float(each_value1))
                            break

            #evalue if the element[0] starts with given year 2 (we want that data)
            elif string_year.startswith(str(year2)):
                #variable will store the value
                each_value2 = 0
                #add to list, the values of sea mm
                while each_value2 == 0:
                    #will go through each possible values and take one (SEA LEVEL MM)
                    #on each line list at given year
                    for i in range(1,len(line)):
                        if line[i] == "":
                            pass
                        else:
                            #add value at our list
                            each_value2 = line[i]
                            values2.append(float(each_value2))
                            break


    #SECOND PART_ANALYSING
    #Getting the max value on each year and average
    print("SEA LEVEL ON", year1)
    print(values1)
    max_1 = max(values1)
    print("The maximun value was", max_1)
    average = sum(values1) / len(values1)
    print("The average was",average,"mm")

    print("SEA LEVEL ON", year2)
    print(values2)
    max_2 = max(values2)
    print("The maximun value was", max_2)
    average2 = sum(values2) / len(values2)
    print("The average was",average2,"mm")

    #Variation
    #Evaluate which max value is bigger
    #AVOID THE ERROR THAT USER FIRST PASS lower year and then current one
    if str(year1) > str(year2):
        var = ((max_1 - max_2) / max_2) * 100
        if var > 0:
            print("Maximum level on", year1, "increases by", str(var))
        elif var < 0:
            print("Maximum level on", year1, "decreases by", str(var))
        else:
            print("Maximum sea level is the same")
    else:
        var = ((max_2 - max_1) / max_1) * 100
        if var > 0:
            print("Maximum level on", year2, "increases by", str(var) + "%")
        elif var < 0:
            print("Maximum level on", year2, "decreases by", str(var) + "%")
        else:
            print("Maximum sea level is the same")

#Start the program
if __name__== "__main__":
    main()
