class A:
    def method(self):
        print('method')

    def caller(self, method):
        method()

    def passer(self):
        self.caller(self.method)


if __name__ == '__main__':
    a = A()
    a.passer()
