def greet(func):
    def inner (*args, **kwargs):
        import time
        st = time.time()

        func(*args,*kwargs)
        et = time.time()
        print(et-st)

    return inner

@greet

def fun(a,b):
    print(a+b)
fun(10,3)

@greet
def sub(x,z):
    print(x-z)
sub(10,3)
