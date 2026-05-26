class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, customer, material, color, price):
        self.customer = customer
        self.material = material
        self.color = color
        self.price = price

    def show_order(self):
        print("\nOrder Information")
        print("Customer:", self.customer.name)
        print("Material:", self.material)
        print("Color:", self.color)
        print("Price:", self.price)

def create_order():
    name = input("Enter customer name: ")
    material = input("Enter material: ")
    color = input("Enter material color: ")
    price = input("Enter estimated price: ")

    customer = Customer(name)
    order = Order(customer, material, color, price)

    order.show_order()


def main():
    print("Atelier Management System")
    print("-------------------------")

    while True:
        print("\n1. Create Order")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_order()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()