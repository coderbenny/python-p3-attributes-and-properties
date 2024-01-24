
class Human():

    species = "Homo Sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0

    def get_age(self):
        print("Retrieving age...")
        return self._age
    
    def set_age(self, age):
        if (type(age) in (int,float)) and (0 <= age <= 120):
            print(f"Setting age to {age}")
            self._age = age
        else:
            print("Age must be a number between 0 and 120.")


    age = property(get_age, set_age,)

producer = Human("Benny")
print(producer.name)
producer.set_age(50)
print(producer.age)
