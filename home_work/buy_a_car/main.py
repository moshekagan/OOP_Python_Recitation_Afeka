from home_work.buy_a_car.Customer import Customer
from home_work.buy_a_car.Store import Store
from home_work.buy_a_car.Vehicle import Vehicle


def main():
    store = Store("vehicles_supply.csv", "customers.csv")

    print("******** All Customers: ********")
    store.print_customers()

    print("\n******** All Vehicles: ********")
    store.print_vehicles()

    new_vehicle = Vehicle([1111111, "Car", "Tesla", "Model Y", 2022, 300000])
    store.add_vehicle(new_vehicle)
    res = store.remove_vehicle(new_vehicle.licence_plate) # res should be True

    print("\n******** All Kias: ********")
    kias = store.get_all_by_manufacturer("Kia")
    store.print_vehicles_list(kias)

    print("\n******** All BMWs: ********")
    BMWs = store.get_all_by_manufacturer("BMW")
    store.print_vehicles_list(BMWs)

    print("\n******** All under 15K: ********")
    less_then_15K = store.get_all_by_price_under(15000)
    store.print_vehicles_list(less_then_15K)

    print("\n******** Most Expensive ********")
    most_expensive = store.get_most_expensive_vehicle()
    most_expensive.print_me()

    new_customer = Customer([71627, "Jichael Jordan", "1901 W Madison St, Chicago", "0501232323", "M"])
    store.add_customer(new_customer)
    store.remove_customer(new_customer.customer_id)


if __name__ == '__main__':
    main()



