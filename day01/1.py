import dis #反汇编

def f():
    lambda: k  #该函数没有参数，返回值为局部变量 k
    k=1         #将局部变量 k 赋值为 1
    print([locals() for k in [0]]) #返回当前作用域内所有局部变量的字典
    assert k==1  #断言语句，用于检查某个条件是否为真。如果条件为真，程序会继续执行；如果条件为假，会抛出 AssertionError 异常
    #查 k 的值是否为 1，由于在列表推导式外部 k 的值被赋值为 1，所以这个断言会通过


dis.dis(f) #此函数接收一个可调用对象（像函数、方法、类等）作为参数，接着对该对象的字节码进行反汇编，输出一系列操作码（opcodes）以及对应的参数。这些操作码属于 Python 虚拟机（Python Virtual Machine，简称 PVM）执行代码时的底层指令

