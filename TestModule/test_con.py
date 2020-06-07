from datetime import datetime

def run_time(func):
    def inner_func(*parm):
        begin_time = datetime.now()
        ret = func(*parm)
        end_time = datetime.now()
        print(end_time - begin_time)
        return ret
    return inner_func

def funcA():
    if 3 < 1 or 2 < 1:
        print(123)


def funcB():
    return 1, 2, 3

@run_time
def funcC():
    set1 = ([i for i in range(1000000)])
    # list1 = [i for i in range(1000000)]
    # print(set1[999999])
    # print(list1[999999])
    for i in set1:
        ix = i


@run_time
def funcD():
    # set1 = ([i for i in range(1000000)])
    list1 = [i for i in range(1000000)]
    # print(set1[999999])
    # print(list1[999999])
    for i in list1:
        ix = i

def funcE():
    print(max(1, 2, 3, 'asdf', 'asdfasdf', key=int))

if __name__ == '__main__':
    funcE()