class A:
    def __init__(self):
        self.a = 'вік'

    def method_a(self):
        print("1488 років")


class B:
    def __init__(self):
        self.b = 'імя'

    def method_b(self):
        print("ім'я пасхалко")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = 'місце народження'

    def method_c(self):
        print("родився в чорному дельфіні")



obj_c = C()


print(obj_c.a)
print(obj_c.b)
obj_c.method_a()
obj_c.method_b()


print(obj_c.c)
obj_c.method_c()
