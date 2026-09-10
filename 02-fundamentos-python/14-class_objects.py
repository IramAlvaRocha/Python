class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
    def work(self):
        return f"{self.name} está trabajando duro"
    
person1 = Person("Iram", 27);
person2 = Person("Fernando", 47);

print(person1.work()) 
print(person2.work()) 