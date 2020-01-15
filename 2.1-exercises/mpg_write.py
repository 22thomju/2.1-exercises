#!/usr/bin/env python3
import csv

#get input from user
def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :      "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

#get user input     
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print()
    print("================================")
    print("The Miles Per Gallon application")
    print("================================")
    print()
    trips = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        trip = []
        trip.append (miles_driven)
        trip.append (gallons_used)
        trip.append (mpg)
        trips.append (trip)
        with open("trips.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(trips)
        with open("trips.csv", newline="") as file:
            reader = csv.reader(file)
            print("Distance" + " " + "Gallons" + " " + "MPG")
            for row in reader:
                print(row[0] + " " + str(row[1]) + " " + str(row[2]))

        more = input("More entries? (y or n): ")
    
    print("Bye")

if __name__ == "__main__":
    main()