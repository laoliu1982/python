import sys
def logtest(msg):
    if(isinstance(msg,str)):
        print('Print Message: '+msg+' ,File: "'+__file__+'", Line '+str(sys._getframe().f_lineno)+' , in '+sys._getframe().f_code.co_name)
    else:
        msg=str(msg)
        print('Print Message: '+msg+' ,File: "'+__file__+'", Line '+str(sys._getframe().f_lineno)+' , in '+sys._getframe().f_code.co_name)

def log2(func):
    print("hi log2")
    def hello2(*args, **kw):
        print("call %s:"%func.__name__)
        return func(*args,**kw)
    print("bye log2")
    #return(func)
    return(hello2)

def log1(func):
    print("hi log1")
    def hello(*args,**kw):
        print('call %s:' %func.__name__)
        return func(*args,**kw)
    print("bye log1")
    return(hello)

@log2
def now():
    print("hello now")

#@log1
def future():
    print("hello future")


def hellotest():
    def inner(*args,**kw):
        print("hello inner")
        return("hello inner return")
        #return (future)
    print("hello test")
    return(inner())
if __name__=='__main__':
    logtest(sys.argv)
    #now()
    #future()
    #print(type(hellotest()))
    #print(hellotest())
    log1(future)()
    now()
