def main():
    r = "Friend"
    print("Hello")
    print(4 + 9)
    print("Good Morning", r)


if __name__ == "__main__":
    main()


# class & object creation
class Animal:
    color = ""
    legs = 0


a1 = Animal()
a1.color = "blue"
a1.legs = 4

a2 = Animal()
a2.color = "brown"
a2.legs = "2"

print(a1.color, a1.legs)
print(a2.color, a2.legs)


# ===========================
class Bird():  # class Bird: also correct
    # def __init__(self,name):
    #     self.name = name
    def fly(self):
        print("bird is flying !")


b1 = Bird()
b1.fly()


class Parrot(Bird):  # inheritance
    def speak(self):
        print("Parrot is speaking")


p1 = Parrot()
p1.speak()
p1.fly()


# ============================
# simple calculator app
class Cal:
    # def __init__(self,a,b)
    #     self.a=a
    #     self.b=b
    def add(self, a, b):
        print(a + b)

    def sub(self, c, d):
        print(c - d)

    def div(self, a, b):
        print(a / b)

    def mul(self, a, b):
        print(a * b)


r = Cal()
r.add(2, 8)
r.sub(4, 1)
r.div(6, 2)
r.mul(3, 2)

# ----------------------------