import calendar
from typing import Optional
import db2
from objects2 import Member, AdventureLocations, Category, ScheduledAdventures, Adventure
from datetime import datetime
from contextlib import closing

##Member Functions
def add_Member():
    firstName = input("First name: ").title()
    lastName = input("Last name: ").title()
    Address = input("Address: ").title()
    City = input("City: ").title()
    State = input("State: ").strip().title()  # Title-case the state to standardize it
    ZipCode = input("ZipCode: ").strip()
    Country = input("Country: ").title()
    PhoneNumber = input("Phone number: ")
    Email = input("Email: ")

    ZipCode = int(ZipCode)

# Create a new member and add to database
    new_member = Member(
    firstName=firstName,
    lastName=lastName,
    Address=Address,
    City=City,
    State=State,  
    ZipCode=ZipCode,
    Country=Country,
    PhoneNumber=PhoneNumber,
    Email=Email,
)

    db2.add_Member(new_member)  
    print(f"Member {new_member.firstName} {new_member.lastName} was added.\n")


def update_member():
    member_id = int(input("Enter the MemberID to update: "))
    
    # Existing Members
    existing_member = db2.get_member_by_id(member_id)
    if not existing_member:
        print("Member not found.")
        return
    
    
    print(f"\nCurrent Information for MemberID {member_id}:")
    print(f"1. First Name: {existing_member.firstName}")
    print(f"2. Last Name: {existing_member.lastName}")
    print(f"3. Address: {existing_member.Address}")
    print(f"4. City: {existing_member.City}")
    print(f"5. State: {existing_member.State}")
    print(f"6. Zip Code: {existing_member.ZipCode}")
    print(f"7. Country: {existing_member.Country}")
    print(f"8. Phone Number: {existing_member.PhoneNumber}")
    print(f"9. Email: {existing_member.Email}")
    
    
    fields_to_update = input("\nEnter the numbers of the fields you want to update (e.g., 1,3,5): ").split(',')
    
    # Update fields
    updated_fields = {}
    for field in fields_to_update:
        if field.strip() == '1':
            updated_fields['firstName'] = input("Enter updated first name: ").title()
        elif field.strip() == '2':
            updated_fields['lastName'] = input("Enter updated last name: ").title()
        elif field.strip() == '3':
            updated_fields['Address'] = input("Enter updated address: ").title()
        elif field.strip() == '4':
            updated_fields['City'] = input("Enter updated city: ").title()
        elif field.strip() == '5':
            updated_fields['State'] = input("Enter updated state: ").strip().title()
        elif field.strip() == '6':
            updated_fields['ZipCode'] = input("Enter updated zip code: ").strip()
        elif field.strip() == '7':
            updated_fields['Country'] = input("Enter updated country: ").title()
        elif field.strip() == '8':
            updated_fields['PhoneNumber'] = input("Enter updated phone number: ")
        elif field.strip() == '9':
            updated_fields['Email'] = input("Enter updated email: ")

    # Create Updated Member Object 
    updated_member = Member(
        MemberID=member_id,
        firstName=updated_fields.get('firstName', existing_member.firstName),
        lastName=updated_fields.get('lastName', existing_member.lastName),
        Address=updated_fields.get('Address', existing_member.Address),
        City=updated_fields.get('City', existing_member.City),
        State=updated_fields.get('State', existing_member.State),
        ZipCode=updated_fields.get('ZipCode', existing_member.ZipCode),
        Country=updated_fields.get('Country', existing_member.Country),
        PhoneNumber=updated_fields.get('PhoneNumber', existing_member.PhoneNumber),
        Email=updated_fields.get('Email', existing_member.Email)
    )

    db2.update_member(updated_member)
    print("Member updated successfully!")


    
def delete_member():
    member_id = int(input("Enter the MemberID to delete: "))
    db2.delete_member(member_id)
    print("Member deleted successfully!")

def display_members():
    sql = '''SELECT MemberID, firstName, lastName, Address, City, State, ZipCode, Country, PhoneNumber, Email
             FROM Members'''
    with closing(db2.conn.cursor()) as c:
        c.execute(sql)
        results = c.fetchall()
        for row in results:  
            print(f"MemberID: {row[0]}, Name: {row[1]} {row[2]}, Address: {row[3]}, {row[4]}, {row[5]} {row[6]}, {row[7]}, Phone: {row[8]}, Email: {row[9]}")

def add_location():
    LocationName = input("Location name: ").title()
    print("Available categories:")

    
    categories = db2.get_all_categories()

   
    if not categories:
        print("No categories found.")
        return

  
    for category in categories:
        print(f"{category[0]}: {category[1]}")  # category[0] is CategoryID, category[1] is CategoryName

    # Enter the category ID
    CategoryID = int(input("Enter Category ID: "))
    Address = input("Address: ").title()
    City = input("City: ").title()
    State = input("State (2 uppercase letters): ").upper()  # Ensure uppercase for state
    ZipCode = input("ZipCode (5 digits): ")

    # Ensure zip code is exactly 5 digits
    while len(ZipCode) != 5 or not ZipCode.isdigit():
        print("Invalid zip code. It must be exactly 5 digits.")
        ZipCode = input("ZipCode (5 digits): ")

    Country = input("Country: ").title()

    # Create a new location object and add it to the database *****
    new_location = AdventureLocations(
        LocationName=LocationName,
        CategoryID=CategoryID,
        Address=Address,
        City=City,
        State=State,
        ZipCode=ZipCode,
        Country=Country
    )

  
    db2.add_AdventureLocations(new_location)
    print(f"Location {new_location.LocationName} was added.")




def update_location():
    location_id = int(input("Enter the LocationID to update: "))
    existing_location = db2.get_location_by_id(location_id)
    
    if not existing_location:
        print("Location not found.")
        return
    
    # Display current location information
    print(f"\nCurrent Information for LocationID {location_id}:")
    print(f"1. Location Name: {existing_location.LocationName}")
    print(f"2. Category ID: {existing_location.CategoryID}")
    print(f"3. Address: {existing_location.Address}")
    print(f"4. City: {existing_location.City}")
    print(f"5. State: {existing_location.State}")
    print(f"6. Zip Code: {existing_location.ZipCode}")
    print(f"7. Country: {existing_location.Country}")
    
    fields_to_update = input("\nEnter the numbers of the fields you want to update (e.g., 1,3,5): ").split(',')
    
    updated_fields = {}
    for field in fields_to_update:
        if field.strip() == '1':
            updated_fields['LocationName'] = input("Enter updated location name: ").title()
        elif field.strip() == '2':
            categories = db2.get_all_categories()
            print("Available categories:")
            for category_id, category_name in categories.items():
                print(f"{category_id}: {category_name}")
            updated_fields['CategoryID'] = int(input("Enter updated category ID: "))
        elif field.strip() == '3':
            updated_fields['Address'] = input("Enter updated address: ").title()
        elif field.strip() == '4':
            updated_fields['City'] = input("Enter updated city: ").title()
        elif field.strip() == '5':
            updated_fields['State'] = input("Enter updated state: ").title()
        elif field.strip() == '6':
            updated_fields['ZipCode'] = input("Enter updated zip code: ").title()
        elif field.strip() == '7':
            updated_fields['Country'] = input("Enter updated country: ").title()

    updated_location = AdventureLocations(
        LocationID=location_id,
        LocationName=updated_fields.get('LocationName', existing_location.LocationName),
        CategoryID=updated_fields.get('CategoryID', existing_location.CategoryID),
        Address=updated_fields.get('Address', existing_location.Address),
        City=updated_fields.get('City', existing_location.City),
        State=updated_fields.get('State', existing_location.State),
        ZipCode=updated_fields.get('ZipCode', existing_location.ZipCode),
        Country=updated_fields.get('Country', existing_location.Country)
    )

    db2.update_location(updated_location)
    print("Location updated successfully!")

def display_locations():
    locations = db2.get_all_locations()  # All locations from the database
    if not locations:
        print("No locations found.")
        return

    print("\nList of Locations:")
    for location in locations:
        print(f"\nLocationID: {location.LocationID}")
        print(f"Location Name: {location.LocationName}")
        print(f"Category ID: {location.CategoryID}")
        print(f"Address: {location.Address}")
        print(f"City: {location.City}")
        print(f"State: {location.State}")
        print(f"ZipCode: {location.ZipCode}")
        print(f"Country: {location.Country}")


def delete_location():
    location_id = int(input("Enter the LocationID to delete: "))
    db2.delete_location(location_id)
    print("Location deleted successfully!")

def add_category():
    category_name = input("Enter the category name: ").title()

    # Create a Category object
    new_category = Category(CategoryName=category_name)

   
    db2.add_category(new_category)
def update_category():
    
    categories = db2.get_all_categories()  

    if categories:
        # Display the available categories
        print("Available categories to edit:")
        for category in categories:
            print(f"{category.CategoryID}: {category.CategoryName}")  # Display CategoryID and CategoryName

        
        category_id = int(input("Enter the CategoryID to update: "))

        
        new_category_name = input("Enter the new category name: ").title()

        
        updated_category = Category(CategoryID=category_id, CategoryName=new_category_name)

        
        db2.update_category(updated_category)
        print(f"Category {category_id} has been updated to '{new_category_name}'.")
    else:
        print("No categories available to edit.")
        
def display_category():
    # All cats
    categories = db2.get_all_categories()  

    if categories:
        print("Available Location Categories:")
        for category in categories:
            print(f"CategoryID: {category.CategoryID}, CategoryName: {category.CategoryName}")
    else:
        print("No categories available.")

def delete_category():

    display_category()  

   
    category_id = int(input("Enter the CategoryID to delete: "))

   
    db2.delete_category(category_id)

    print(f"Category with CategoryID {category_id} has been deleted.")


def add_adventure():
    
    locations = db2.get_all_locations()

    print("Available Locations:")
    # Display locations
    for location in locations:
        
        print(f"LocationID: {location.LocationID}, Location Name: {location.LocationName}")

    
    location_id = int(input("Enter the LocationID for the adventure: "))

    
    month = int(input("Enter the Month (1-12): "))
    day = int(input("Enter the Day (1-31): "))
    year = int(input("Enter the Year: "))

    # Validate month, day, and time
    if not (1 <= month <= 12):
        print("Invalid month. Please enter a month between 1 and 12.")
        return

    # Check if the day is valid for the selected month
    if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
        print("Invalid day. Please enter a valid day for the month.")
        return
    elif month in [4, 6, 9, 11] and not (1 <= day <= 30):
        print("Invalid day. Please enter a valid day for the month.")
        return
    elif month == 2 and not (1 <= day <= 29):  # Assuming leap years are considered
        print("Invalid day. Please enter a valid day for February.")
        return

    # Handle time input and validation***pain
    while True:
        time_input = input("Enter the time in military format (HH:MM): ")
        if is_valid_time(time_input):
            break
        else:
            print("Invalid time format. Please enter the time in military format (HH:MM).")
    
    
    print(f"Adventure scheduled for {month}/{day}/{year} at {time_input}!")

    
    new_adventure = Adventure(
        LocationID=location_id,
        Month=month,
        Day=day,
        Year=year,
        Time=time_input  # Ensure time_input is passed correctly
    )
    
    
    db2.add_adventure(new_adventure)
    print(f"Adventure scheduled at LocationID {location_id} on {month}/{day}/{year} at {time_input}.")

def update_adventure():
    adventures = db2.get_all_adventures()
    print("Scheduled Adventures:")
    for adventure in adventures:
        print(f"AdventureID: {adventure[0]}, LocationID: {adventure[1]}, Date: {adventure[2]}/{adventure[3]}/{adventure[4]}, Time: {adventure[5]}")

    adventure_id = int(input("Enter AdventureID to update: "))
    adventure = db2.get_adventure_by_id(adventure_id)
    if adventure:
        
        LocationID = int(input("Enter new LocationID: "))
        
        
        Month = int(input("Enter new Month (1-12): "))
        while Month < 1 or Month > 12:
            print("Invalid month. It must be between 1 and 12.")
            Month = int(input("Enter new Month (1-12): "))
        
        
        Day = int(input("Enter new Day: "))
        while not is_valid_day(Month, Day):  
            print("Invalid day for this month. Please try again.")
            Day = int(input("Enter new Day: "))

        
        Year = int(input("Enter new Year: "))
        Time = input("Enter new Time (military format HH:MM): ")
        while not is_valid_time(Time):
            print("Invalid time format. Please use military time (HH:MM).")
            Time = input("Enter new Time (military format HH:MM): ")

        
        updated_adventure = ScheduledAdventures(
            AdventureID=adventure_id, 
            LocationID=LocationID, 
            Month=Month, 
            Day=Day, 
            Year=Year, 
            Time=Time
        )
        
        
        db2.update_adventure(updated_adventure)
        print("Adventure updated successfully.")


def display_adventures():
    adventures = db2.get_all_adventures()
    print("Scheduled Adventures:")
    for adventure in adventures:
        print(f"AdventureID: {adventure[0]}, LocationID: {adventure[1]}, Date: {adventure[2]}/{adventure[3]}/{adventure[4]}, Time: {adventure[5]}")

def delete_adventure():
    adventures = db2.get_all_adventures()
    print("Scheduled Adventures:")
    for adventure in adventures:
        print(f"AdventureID: {adventure[0]}, LocationID: {adventure[1]}, Date: {adventure[2]}/{adventure[3]}/{adventure[4]}, Time: {adventure[5]}")

    adventure_id = int(input("Enter AdventureID to delete: "))
    db2.delete_adventure(adventure_id)
    print(f"Adventure with ID {adventure_id} deleted successfully.")

def is_valid_day(month, day):
    # Check valid days in each month
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    # Handle leap year for February
    if month == 2:
        if (year := 2024) % 4 == 0:  # Example leap year check for simplicity
            days_in_month[2] = 29
    return day <= days_in_month.get(month, 31)

def is_valid_time(time):
    # Check if the time is in military format (HHMM)
    if len(time) != 4 or not time.isdigit():
        return False
    hours, minutes = int(time[:2]), int(time[2:])
    return 0 <= hours < 24 and 0 <= minutes < 60




# Menu options
def display_menu():
    print("MENU OPTIONS")
    
    # Left column (options 1-7)
    left_column = [
        "1 – Add Member",
        "2 – Edit Member",
        "3 – Delete Member",
        "4 - Display Members",
        "5 - Add Adventure Location",
        "6 - Edit Adventure Location",
        "7 - Display Adventure Location",
        "8 - Delete Adventure Location",
        "9 - Add Location Category"
    ]
    
    # Right column (options 8-13)
    right_column = [
        "10 - Edit Location Category",
        "11 - Display Location Category",
        "12 - Delete Location Category",
        "13 - Schedule an Adventure",
        "14 - Edit a Scheduled Adventure",
        "15 - Display Scheduled Adventures",
        "16 - Delete Scheduled Adventure",
        "17 - Menu",
        "18 - Exit Program"
    ]
    
    # Print both columns side by side***Learned this! Cool!
    for i in range(max(len(left_column), len(right_column))):
        left_option = left_column[i] if i < len(left_column) else ""
        right_option = right_column[i] if i < len(right_column) else ""
        print(f"{left_option:<40} {right_option}")

def display_seperator():
    print("=" * 84)

def display_title():
    title = "Family Adventures"
    print(f"{title.center(84)}")

def display_space():
    print(" ")

def main():
    db2.connect()  # Database Connection
    display_seperator()
    display_title()
    display_space()
    display_menu()
    display_seperator()

    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            option = -1
            
        if option == 1:
            add_Member()
        elif option == 2:
            update_member()
        elif option == 3:
            delete_member()
        elif option == 4:
            display_members()
        elif option == 5:
            add_location()
        elif option == 6:
            update_location()
        elif option == 7:
            display_locations()
        elif option == 8:
            delete_location()
        elif option == 9:
            add_category()
        elif option == 10:
            update_category()
        elif option == 11:
            display_category()
        elif option == 12:
            delete_category()
        elif option == 13:
            add_adventure()
        elif option == 14:
            update_adventure()
        elif option == 15:
            display_adventures()
        elif option == 16:
            delete_adventure()
        elif option == 17:
            display_menu()
        elif option == 18:
            db2.close()
            print("Goodbye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()












    
    

