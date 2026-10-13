class Player:
    def __init__(self):
        while True:
            self.name = input("Enter your full name [First name and Last name]: ").strip().title().split()
            if len(self.name) != 2:
                continue
            else:
                break 
        print(f"Your name is: {self.name[0]} {self.name[1]}")

        