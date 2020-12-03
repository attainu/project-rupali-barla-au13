class parking_lot:
    def __init__(self):
        self.slots_capacity = 0
        self.slots_occupied = 0

    def Create(self, slots_capacity):
        self.parking_slots = ['-1' for _ in range(slots_capacity)]
        self.slots_capacity = slots_capacity
        return self.slots_capacity

    def AllocateSlots(self):
        for slot_no in range(self.slots_capacity):
            if self.parking_slots[slot_no] == '-1':
                return slot_no
            else:
                continue

    def Park(self, reg_no, color):
        if self.slots_occupied < self.slots_capacity:
            slot_no = self.AllocateSlots()
            self.parking_slots[slot_no] = reg_no+"  "+color
            self.slots_occupied += 1
            return slot_no + 1
        else:
            return -1

    def Leave(self, slot_no):
        if slot_no > self.slots_capacity:
            return -1
        elif self.slots_occupied > 0 and self.parking_slots[slot_no-1] != '-1':
            self.parking_slots[slot_no-1] = '-1'
            self.slots_occupied -= 1
            return True
        else:
            return False
    
    def Status(self):
        print("Slot No. Registration No. Colour")
        for i in range(len(self.parking_slots)):
            if self.parking_slots[i] != '-1':
                print("   "+str(i+1)+"\t   "+str(self.parking_slots[i]))
            else:
                continue
    
    def Reg_No_By_Color(self, color):
        reg_nos = []
        for i in range(self.slots_capacity):
            if color in self.parking_slots[i]:
                val = self.parking_slots[i]
                reg_nos.append(val[:(len(val) - len(color) - 1)])
        return reg_nos

    def Slot_No_By_Color(self, color):
        slot_nos = []
        for slot_no in range(self.slots_capacity):
            if color in self.parking_slots[slot_no]:
                slot_nos.append(str(slot_no + 1))
        return slot_nos

    def Slot_No_By_Reg_No(self, reg_no):
        for slot_no in range(self.slots_capacity):
            if reg_no in self.parking_slots[slot_no]:
                return slot_no + 1
            else:
                continue
        return -1
