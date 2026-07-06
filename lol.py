class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


def main():
    obj = Calculator(int(input("Enter a number:")),int(input("Enter a number:")))
    print(obj.add())

if __name__ == '__main__':
    main()