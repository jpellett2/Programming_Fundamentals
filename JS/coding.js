/* This is the javascript code for the final project 
 File: /jpellett2_Final/finalproject.html */
 
 function numberofhouses() {
 // Declare variables
   var bedrooms;
   var bathrooms;
   var housesize;
   var windows;
   var garage;
   var garagesize;
   var basement;
   var count = 0;
   var cost;
   var insulationcost;
   var labor;
   var windowcost;
   var windowinstallationcost;
   var numberofhouses = prompt("How many houses do you want to build?");


for (var count = 0; count < numberofhouses; count++) {
    var housesize = prompt("What is the desired square footage of the house?");
    var bedrooms = prompt("How many bedrooms should the house have?");
    var bathrooms = prompt("How many bathrooms?");
    var windows = prompt("How many windows should the house have?");
    var basement = prompt("Do you want a basement? Y or N");
    var garage = prompt("Do you want a garage? Y or N");
    
   
   
    //Converting to numbers //
    numberofhouses = Number(numberofhouses);
    bedrooms = Number(bedrooms);
    bathrooms = Number(bathrooms);
    windows = Number(windows);
    housesize = Number(housesize);
    
    // Calculate cost based on user input (All numbers are based on average quality materials)
    // ...
    var insulationcost = housesize * 3.50;
    var windowcost = windows * 500;
    var windowinstallationcost = windowcost * 0.15;
    var labor = 150 * housesize;
    var sidingcost = 12 * housesize;
    var roofcost = 400 * housesize;
    var bathroomcost = bathrooms * 6000;
    var cost = insulationcost + windowcost + windowinstallationcost + labor + sidingcost + roofcost + bathroomcost; 

    // Display house details
    
    document.write("For house #" + (count + 1) + ":");
    document.write("\n");
    document.write("Square footage: " + housesize);
    document.write("\n");
    document.write(bedrooms + " bedrooms");
    document.write("\n");
    document.write(bathrooms + " bathrooms");
    document.write("\n");
    document.write(windows + " windows");
    document.write("\n");
    
    if (basement === 'y') {
    document.write("Basement: yes ");
    document.write("\n");
    }
    if (garage === 'y') {
    var garagesize = prompt("What square footage do you want for the garage?");
    document.write("Garage: yes ");
    document.write("\n");
    document.write("Garage size: " + garagesize + " square feet");
    document.write("\n");
    }
    document.write("Cost: $" + cost);
    document.write("\n\n");
    
  }
 }  
 numberofhouses();