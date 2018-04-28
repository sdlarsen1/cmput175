# implement HandHeldClicker
class HandHeldClicker:
    def __init__(self):
        self.count = 0
    
    def push(self):
        self.count += 1
        
    def reset(self):
        self.count = 0
    
    def get_count(self):
        return self.count

clicker = HandHeldClicker()

#text interface
def main():
    print("Hand-Held Clicker starts.")
    action = input("Action:")
    while action in "pre":
        #push button
        if action == "p":
            clicker.push()
            print("Count:" + str(clicker.get_count()))
        #reset clicker
        elif action == "r":
            clicker.reset()
            print("Count:" + str(clicker.get_count()))
        #terminate cliker
        elif action == "e":
            print("Hand-Held Clicker ends.")
            break

        action = input("Action:")
    
if __name__ == "__main__":
    main()
