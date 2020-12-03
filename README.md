Parking Lot :-

Designed a parking lot using Python

Description :

It creates a parking lot with given number of slots.  

Parking_Lot.py script defines the following functions :-

1) Create - Given n number of slots, creates a parking lot

2) Park - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".

3) Leave - Removes vehicle from slot number x.

4) Status - Prints the slot number, registration number and color of the parked vehicles.

5) Reg_No_By_Color - Gives the registration numbers of all cars of a particular color.

6) Slot_No_By_Color - Gives the slot numbers of all cars of a particular color.

7) Slot_No_By_Reg_No - Gives the slot number by providing registration number.

Parking_Lot.py can be run through shell or through file containing test cases. An input test case file commands.txt has been provided in repo as mentioned in project guidelines.

To Run Project :-

1) Clone the repository https://github.com/attainu/project-rupali-barla-au13/tree/dev

2) Install Python

3) Install flake8 library:

i) pip install flake8

ii) goto root directory where parkinglot.py file is present.

iii) Run python -m flake8 command and check for any errors:

iv) like I got blank line contains whitespace error, to ignore that use #noqa at the end 

4) Run parking_main.py to run without input test case file. This opens a shell where you can write your commands like - create_parking_lot 6, leave 4, status etc as provided in the project guidelines.

5) To run with a file, execute python parking_main.py -f commands.txt. You can modify the test cases.

Technologies used :-

Project is created with : -

• Python: 3.8.5

• Flake8 (for linting)