Parking Lot :-

Designed a parking lot using Python

Description :

It creates a parking lot with given number of slots. The vehicles follow Greedy approach while being parked in the slots.

parkinglot.py script defines the following functions :-

1) create_parking_space - Given n number of slots, creates a parking lot

2) parking_of_vehicle - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".

3) show_all_parked_cars - Prints the slot number, registration number and color of the parked vehicles.

4) leave_parking - Removes vehicle from slot number x.

5) get_slot_no_by_registration_no - Gives the slot number by providing registration number.

6) get_slot_no_of_all_car_by_colour - Gives the slot numbers of all cars of a particular colour.

7) get_regno_of_all_car_by_colour - Gives the registration numbers of all cars of a particular colour.

parkinglot.py can be run through shell or through file containing test cases. An example file run_test_case.txt has been provided in repo.

To Run Program :-

1) Clone the repository https://github.com/attainu/project-rupali-barla-au13/tree/dev

2) Install Python

3) Install flake8 library:

o pip install flake8
o goto root directory where parkinglot.py file is present.
o Run python -m flake8 command and check for any errors:
o like I got no newline error, to ignore that use #noqa at the end 

4) Run python park_command.py to run without input test case file. This opens a shell where you can write your commands like - create_parking_lot 6, leave 4, etc as provided in the project guidelines.

5) To run with a file execute python park_command.py -f run_test_case.txt. You can modify the test cases.

Technologies used :-

Project is created with : -
• Python: 3.8.5
• Flake8 (for linting)