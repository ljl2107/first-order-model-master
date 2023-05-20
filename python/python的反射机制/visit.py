import commons


def run():
    inp = input("请输入您想访问的页面url:").strip()
    modules, func = inp.split("/")
    obj = __import__("lib."+modules,fromlist=True)#加了lib 会报错
    if hasattr(obj,func):
        func = getattr(obj,func)
        func()
    else:
        print("404")
run()


# getattr函数接受两个参数 第一个是对象或模块 第二个是字符串！
# 在对象或模块中寻找叫字符串名的成员，然后吧获得的结果赋值给func变量
# 实际上func指向commons里的某个函数
# hasattr 用于判断是否拥有成员
# __import__(modules) 让程序导入了modules这个变量保存的字符串同名的模块
#https://www.lmlphp.com/user/75355/article/item/784582/


