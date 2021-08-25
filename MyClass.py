class Myclass:

    b = "on class"

def __init__(self):
    self.a = "on instance"
    print(self.a)
    print(Myclass.b)
    print(self.b)
    self.a ="re-bound"
    self.b = "new on instance"
    