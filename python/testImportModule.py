__author__ = 'Jim'

class A:
    def fun(self):
        print 1
    def get(self):
        b=getattr(self, "fun")
        b()


if __name__ == "__main__":
    a=A()
    # module_path = "test.testGetAttr"
    # mod = __import__("test.testGetAttr")
    # components = module_path.split('.')
    # print components
    # for comp in components[1:]:
    #     mod = getattr(a, "fun")
    #     print mod
    a.get()
