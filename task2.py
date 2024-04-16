class House:  # новый класс House

    def __init__(self):  # инициализатор для класса House,
        self.numberOfFloors = 0  # который задает атрибут этажности self.numberOfFloors = 0

    def setNewNumberOfFloors(self, numberOffloors):  # метод setNewNumberOfFloors(floors),
        self.numberOfFloors = (numberOffloors)  # который будет изменять атрибут numberOfFloors на параметр floors
        print('numberOfFloors:', numberOffloors)


my_floor = House()
my_floor.setNewNumberOfFloors(numberOffloors=7)
