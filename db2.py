import sqlite3
from contextlib import closing
from objects2 import Member, AdventureLocations, Category, ScheduledAdventures, Adventure

# Global variable for the database connection
conn = None

# Database connection
def connect():
    global conn
    try:
        conn = sqlite3.connect('family_adventures.db')  
        print("Database connection established.")
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        raise
def get_db_connection():
    # Modify the path to your actual database
    conn = sqlite3.connect('family_adventures.db')  
    return conn
#Close connection
def close():
    if conn:
        conn.close()
        print("Database connection closed.")

def get_member_by_id(member_id):
    sql = '''
    SELECT MemberID, firstName, lastName, Address, City, State, ZipCode, Country, PhoneNumber, Email
    FROM Members WHERE MemberID = ?
    '''
    with conn:
        cur = conn.cursor()
        cur.execute(sql, (member_id,))
        row = cur.fetchone()
        if row:  # Check if a result is found
            return Member(
                MemberID=row[0],        
                firstName=row[1],       
                lastName=row[2],        
                Address=row[3],         
                City=row[4],            
                State=row[5],           
                ZipCode=row[6],         
                Country=row[7],         
                PhoneNumber=row[8],     
                Email=row[9]            
            )
    # If no member is found, return None
    return None

# Update Member 
def update_member(updated_member):
    sql = '''UPDATE Members
             SET firstName = ?, lastName = ?, Address = ?, City = ?, State = ?, ZipCode = ?, Country = ?, PhoneNumber = ?, Email = ?
             WHERE MemberID = ?'''

    with closing(conn.cursor()) as c:
        c.execute(sql, (
            updated_member.firstName,
            updated_member.lastName,
            updated_member.Address,
            updated_member.City,
            updated_member.State,
            updated_member.ZipCode,
            updated_member.Country,
            updated_member.PhoneNumber,
            updated_member.Email,
            updated_member.MemberID  
        ))
        conn.commit()  

#Delete member
def delete_member(member_id):
    sql = '''DELETE FROM Members WHERE MemberID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (member_id,))
        conn.commit()
#Add Location
def add_AdventureLocations():
    LocationName = input("Location name: ").title()
    print("Available categories:")
    
    categories = db2.get_all_categories()
    
    for category in categories:
        print(f"{category[0]}: {category[1]}")  # category[0] is CategoryID, category[1] is CategoryName

    
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

    # Create a new location object and add it to the database (Important)
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
    
#Adds location
def add_AdventureLocations(new_location):
    sql = '''INSERT INTO AdventureLocations (LocationName, CategoryID, Address, City, State, ZipCode, Country)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    
    
    with closing(conn.cursor()) as c:
        c.execute(sql, (new_location.LocationName, new_location.CategoryID, new_location.Address,
                        new_location.City, new_location.State, new_location.ZipCode, new_location.Country))
        conn.commit()  
        print(f"Location {new_location.LocationName} was added.")  # Optional: confirm the addition-my opinion needed XD
#Get Categories
def get_all_categories():
    sql = '''SELECT CategoryID, CategoryName FROM LocationCategorys'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        return c.fetchall()  

def update_location(location):
    sql = '''UPDATE AdventureLocations
             SET LocationName = ?, CategoryID = ?, Address = ?, City = ?, State = ?, ZipCode = ?, Country = ?
             WHERE LocationID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (location.LocationName, location.CategoryID, location.Address, location.City, 
                        location.State, location.ZipCode, location.Country, location.LocationID))
        conn.commit()

def delete_location(location_id):
    sql = '''DELETE FROM AdventureLocations WHERE LocationID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (location_id,))
        conn.commit()

        
def get_location_by_id(location_id):
    sql = '''SELECT LocationID, LocationName, CategoryID, Address, City, State, ZipCode, Country
             FROM AdventureLocations WHERE LocationID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (location_id,))
        row = c.fetchone()
        if row:
            return AdventureLocations(
                LocationID=row[0],
                LocationName=row[1],
                CategoryID=row[2],
                Address=row[3],
                City=row[4],
                State=row[5],
                ZipCode=row[6],
                Country=row[7]
            )
    return None


def get_all_locations():
    sql = '''SELECT LocationID, LocationName, CategoryID, Address, City, State, ZipCode, Country
             FROM AdventureLocations'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        rows = c.fetchall()
        locations = []
        for row in rows:
            location = AdventureLocations(
                LocationID=row[0],
                LocationName=row[1],
                CategoryID=row[2],
                Address=row[3],
                City=row[4],
                State=row[5],
                ZipCode=row[6],
                Country=row[7]
            )
            locations.append(location)
        return locations

# Get all categories from the LocationCategorys table
def get_all_categories():
    sql = '''SELECT CategoryID, CategoryName FROM LocationCategorys'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        rows = c.fetchall()
        # Convert each row into a Category object
        categories = [Category(CategoryID=row[0], CategoryName=row[1]) for row in rows]
        return categories

# Add a new category
def add_category(category):
    sql = '''INSERT INTO LocationCategorys (CategoryName)
             VALUES (?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (category.CategoryName,))
        conn.commit()
        print(f"Category '{category.CategoryName}' added successfully.")

# Update an existing category
def update_category(category):
    sql = '''UPDATE LocationCategorys
             SET CategoryName = ?
             WHERE CategoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (category.CategoryName, category.CategoryID))
        conn.commit()
        print(f"Category ID {category.CategoryID} updated to '{category.CategoryName}'.")

def delete_category(category_id):
    sql = '''DELETE FROM LocationCategorys WHERE CategoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (category_id,))
        conn.commit()  # Save the changes to the database



# Get scheduled adventures
def get_all_adventures():
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ScheduledAdventures")  # Your actual query
        adventures = cursor.fetchall()
        return adventures

# Get adventure by AdventureID
def get_adventure_by_id(adventure_id):
    with closing(get_db_connection()) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM ScheduledAdventures WHERE AdventureID = ?", (adventure_id,))
        return c.fetchone()

# Function to get all locations (corrected)
def get_all_locations():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AdventureLocations")
    locations = cursor.fetchall()
    cursor.close()

    # Create AdventureLocations objects from the results
    adventure_locations = [AdventureLocations(*location) for location in locations]
    return adventure_locations


# Add adventure
def add_adventure(adventure):
    cursor = conn.cursor()
    sql = '''INSERT INTO ScheduledAdventures (LocationID, Month, Day, Year, Time)
             VALUES (?, ?, ?, ?, ?)'''
    cursor.execute(sql, (adventure.LocationID, adventure.Month, adventure.Day, adventure.Year, adventure.Time))
    conn.commit()
    cursor.close()

# Update an existing adventure
def update_adventure(adventure):
    sql = '''UPDATE ScheduledAdventures
             SET LocationID = ?, Month = ?, Day = ?, Year = ?, Time = ?
             WHERE AdventureID = ?'''
    with closing(get_db_connection()) as conn:
        c = conn.cursor()
        c.execute(sql, (adventure.LocationID, adventure.Month, adventure.Day, adventure.Year, adventure.Time, adventure.AdventureID))
        conn.commit()

# Delete an adventure by AdventureID
def delete_adventure(adventure_id):
    sql = "DELETE FROM ScheduledAdventures WHERE AdventureID = ?"
    with closing(get_db_connection()) as conn:
        c = conn.cursor()
        c.execute(sql, (adventure_id,))
        conn.commit()

        
    

