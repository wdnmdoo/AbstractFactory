from Implement import Factory1,Factory2

f1 = Factory1.Factory1()
f2 = Factory2.Factory2()
p1Animal = f1.newAnimal()
p1Animal.show()
p2Plant = f2.newPlant()
p2Plant.show()