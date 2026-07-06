class Calculator:
    def __init__(self,a,c):
        self.a = a
        self.c = c

    def add(self):
        return self.a + self.c
    
    def sub(self):
        return self.a - self.c

    def mul(self):
        return self.a * self.c

    def div(self):
        return self.a / self.c


def main():
    obj = Calculator(int(input("Enter a number:")),int(input("Enter a number:")))
    print(obj.add())

if __name__ == '__main__':
    main()