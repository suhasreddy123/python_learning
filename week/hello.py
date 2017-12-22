x=2+2
print(x)

class utils:
    def add(a,b):
        return a+b

    def square(x):
        return x**2

    def mean(arr):
        return sum(arr)/len(arr)

if __name__ == '__main__':
    u =utils
    print(u.add(2,3))
    print(u.square(5))
    print(u.mean([5,32,5]))