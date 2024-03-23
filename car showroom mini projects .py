class Car:
    def __init__(self, make, model, year, price, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = available

class Showroom:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def sell_car(self, make, model):
        for car in self.inventory:
            if car.make == make and car.model == model and car.available:
                car.available = False
                return car
        return None

    def display_inventory(self):
        print("Available Cars:")
        for car in self.inventory:
            if car.available:
                print(f"{car.year} {car.make} {car.model} - ${car.price}")

def main():
    showroom = Showroom()

    # Adding some initial cars to the showroom
    showroom.add_car(Car("Toyota", "Camry", 2022, 1000000))
    showroom.add_car(Car("Honda", "venue", 2021, 1200000))
    showroom.add_car(Car("maruti suzuki", "Shift", 2020, 700000))

    while True:
        print("\n1. Add Car\n2. Sell Car\n3. Display Inventory\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter make of the car: ")
            model = input("Enter model of the car: ")
            year = int(input("Enter year of the car: "))
            price = float(input("Enter price of the car: "))
            showroom.add_car(Car(make, model, year, price))
            print("Car added successfully!")
        
        elif choice == "2":
            make = input("Enter make of the car to sell: ")
            model = input("Enter model of the car to sell: ")
            sold_car = showroom.sell_car(make, model)
            if sold_car:
                print(f"{sold_car.year} {sold_car.make} {sold_car.model} sold successfully!")
            else:
                print("Car not found or not available.")

        elif choice == "3":
            showroom.display_inventory()

        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
