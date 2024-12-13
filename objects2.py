from dataclasses import dataclass
import calendar
from typing import Optional

class Member:
    def __init__(self,
                 MemberID: Optional[int] = None,
                 firstName: str = "",
                 lastName: str = "",
                 Address: str = "",
                 City: str = "",
                 State: str = "",
                 ZipCode: int = 0,
                 Country: str = "",
                 PhoneNumber: Optional[int] = None,
                 Email: str = ""):
        self.MemberID = MemberID
        self.firstName = firstName
        self.lastName = lastName
        self.Address = Address
        self.City = City
        self.State = State
        self.Country = Country
        self.PhoneNumber = PhoneNumber
        self.Email = Email

        # Validate state length
        if len(State) != 2:
            raise ValueError(f"State must be a 2-character string. You entered: '{State}'")
        
        # Validate ZipCode
        if not self._validate_zipcode(ZipCode):
            raise ValueError(f"ZipCode must be a 5-digit number. You entered: {ZipCode}")
        self.ZipCode = ZipCode

    @staticmethod
    def _validate_zipcode(zipcode: int) -> bool:
        return 10000 <= zipcode <= 99999
    

class Category:
    def __init__(self, CategoryID=None, CategoryName=""):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName

    def __str__(self):
        return f"CategoryID: {self.CategoryID}, CategoryName: {self.CategoryName}"

class AdventureLocations:
    def __init__(self, LocationID, LocationName, CategoryID, Address, City, State, ZipCode, Country):
        self.LocationID = LocationID
        self.LocationName = LocationName
        self.CategoryID = CategoryID
        self.Address = Address
        self.City = City
        self.State = State
        self.ZipCode = ZipCode
        self.Country = Country
class Adventure:
    def __init__(self, LocationID, Month, Day, Year, Time):
        self.LocationID = LocationID
        self.Month = Month
        self.Day = Day
        self.Year = Year
        self.Time = Time


class ScheduledAdventures:
    def __init__(self, AdventureID, LocationID, Month, Day, Year, Time):
        self.AdventureID = AdventureID
        self.LocationID = LocationID
        self.Month = Month
        self.Day = Day
        self.Year = Year
        self.Time = Time
    
   
