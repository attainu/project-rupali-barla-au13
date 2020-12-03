from Parking_Lot import parking_lot
import argparse


class parking_main(parking_lot):
    def instructions(self, command):
        if command.startswith("create_parking_lot"):
            value = int(command.split(' ')[1])
            output = self.Create(value)
            print("Created a parking lot with "+str(output)+" slots")

        elif command.startswith("park"):
            reg_no = command.split(' ')[1]
            color = command.split(' ')[2]
            output = self.Park(reg_no, color)
            if output == -1:
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: "+str(output))

        elif command.startswith("leave"):
            slot_no = int(command.split(' ')[1])
            recent_status = self.Leave(slot_no)
            if recent_status == -1:
                print("Slot number "+str(slot_no)+" is not available")
            elif recent_status:
                print("Slot number "+str(slot_no)+" is free")
            else:
                print("Slot number "+str(slot_no)+" is already free")

        elif command.startswith("status"):
            self.Status()

        elif command.startswith("registration_numbers_for_cars_with_colour"):
            color = command.split(' ')[1]
            reg_no = self.Reg_No_By_Color(color)
            print(', '.join(reg_no))

        elif command.startswith("slot_numbers_for_cars_with_colour"):
            color = command.split(' ')[1]
            slot_no = self.Slot_No_By_Color(color)
            print(', '.join(slot_no))

        elif command.startswith("slot_number_for_registration_number"):
            reg_no = command.split(' ')[1]
            slot_no = self.Slot_No_By_Reg_No(reg_no)
            if slot_no == -1:
                print("Not found")
            else:
                print(slot_no)

        elif command.startswith("exit"):
            print("Thank You. Please Come Again !! ")
            exit()

    def main_func(self):
        Parking_Lot = parking_main()
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", dest="srcfile", help="Input")
        args = parser.parse_args()

        if args.srcfile:
            with open(args.srcfile) as f:
                for command in f:
                    command = command.rstrip('\n')
                    Parking_Lot.instructions(command)
        else:
            while True:
                command = input("$ ")
                Parking_Lot.instructions(command)


if __name__ == "__main__":
    testingCommands = parking_main()
    print("Welcome !!")
    testingCommands.main_func()
