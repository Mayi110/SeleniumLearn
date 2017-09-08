class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.name, self.type)

    def open_restaurant(self):
        print('正在营业')

    def set_number_served(self, set_number):
        self.number = set_number
        print(self.number, '人在这里就餐过')

    def increment_number_served(self, increment_number):
        self.number += increment_number
        print(self.number, '人可以接待')

res = Restaurant('1', '五星级')
res.set_number_served(7)
res.increment_number_served(5)


class IceCreamStand(Restaurant):
    def __init__(self, *flavors):
        self.flavors = flavors

    def show_kinds(self):
        print('口味种类：', self.flavors)

IceCreamStand('apple', 'orange').show_kinds()
a = IceCreamStand()
a.set_number_served(9)