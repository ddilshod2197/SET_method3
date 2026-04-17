# DISCARD
class MySet:
    def __init__(self):
        self.data = []

    def discard(self, value):
        new_data = []
        for item in self.data:
            if item != value:
                new_data.append(item)
        self.data = new_data

    def show(self):
        print(self.data)

s = MySet()
s.data = [1, 2, 3]

s.discard(2)
s.show(

s.discard(10)  
s.show()       
