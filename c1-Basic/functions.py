# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1,arg2):
    print(arg1,"",arg2)

#TODO: function that return a value
def cube(X):
    return X*X*X

#TODO: function with default value for an argument
def power(num, x=2):
    result = 1;
    for i in range(x):
        result = result * num
    return result

#TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1())
print(func1)

func2(10,12)
print(func2(10,13))

print(cube(6))

print(power(3))
print(power(2,4))
print(power(x=3, num=4))

print(multi_add(4,5,10,4))