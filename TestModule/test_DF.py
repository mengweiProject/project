import numpy as np
import pandas as pd
import collections

def calc_loc1():
    info_dict = {'name': ['亚瑟', '妲己', '夏侯惇', '百里守约'],
                 'age': [18, 28, 32, 25],
                 'gender': ['male', 'female', 'male', 'male']}
    t_df = pd.DataFrame(info_dict, index=list(range(len(info_dict['name']))))
    print(t_df)
    print('*' * 20)
    print(t_df.loc[0, 'name'])
    print('*' * 20)
    print(t_df.iloc[0])
    print('*' * 20)
    print(t_df['age'][0:3])
    print('*' * 20)
    print(t_df.loc[0:2, 'name'])
    print('*' * 20)
    print(t_df.iloc[0:2])

def calc_DF2():
    info_df = pd.DataFrame(np.arange(72).reshape(8, 9),
                           columns=list('ABCDEFGHI'))
    print(info_df['A'])

def test_df3():
    info_df = pd.DataFrame({'name': ['亚瑟', '妲己', '夏侯惇', '百里守约', '廉颇', '后裔'],
                 'age': [18, 28, 32, 25, 28, 23],
                 'gender': ['male', 'female', 'male', 'male', 'male', 'male'],
                    'position': ['战士', '法师', '坦克', '射手', '坦克',  '射手']})
    # print(info_df)
    # print(info_df.loc[3:5, ['name', 'position']])
    # print(info_df[(info_df['age'] <= 30)&(info_df['position'] == '射手')].loc[:, ['name', 'gender']])
    print(info_df.loc[0, 'name'])

def test_df4():
    info_df = pd.DataFrame({'name': ['亚瑟', '妲己', '夏侯惇', '百里守约', '廉颇', '后裔'],
                 'age': [18, 28, 32, 25, 28, 23],
                 'gender': ['male', 'female', 'male', 'male', 'male', 'male'],
                    'position': ['战士', '法师', '坦克', '射手', '坦克',  '射手']})
    print(info_df)
    print('*******************')
    # print(info_df.loc[:, 'name'][1])
    print(info_df[info_df["name"] == "后裔"]["age"] * 100)


def t_df5():
    info_df = pd.DataFrame({"NAME": [None]})
    # d = {"name": ""}
    print(info_df)
    # # s = info_df["name"] if len(info_df["name"]) > 0 else "--"
    # s = info_df["name"] if d["name"] else "--"
    # print(s)
    d = info_df.iloc[0, :].to_dict()
    ds = {}
    print(d)


def create_df():
    df = pd.DataFrame([{"a": 1, "b": 2, "name": "字母"},
                       {"c": 3, "d": 4, "number": "很多"},
                       {"e": 5, "f": 6, "order": "随机"}])
    df2 = pd.DataFrame([{"name": "组合1", "age": "2", "time": "2018-05-06", "value": "1023", "type": "port"},
                        {"name": "组合2", "age": "4", "time": "2017-05-06", "value": "1024", "type": "port"},
                        {"name": "组合3", "age": "5", "time": "2016-05-06", "value": "1025", "type": "port"},
                        {"name": "组合4", "age": "6", "time": "2015-05-06", "value": "1026", "type": "port"},
                        {"name": "组合5", "age": "8", "time": "2014-05-06", "value": "1027", "type": "port"},
                        {"name": "组合6", "age": "10", "time": "2013-05-06", "value": "1028", "type": "port"}],
                       index=range(11, 17),
                       columns=["A", "B", "C", "D", "E", "F"])
    print(df2)
    print(df2.index.values)
    print(df2.index.values[0])
    return


def test_df1():
    df1 = pd.DataFrame([{"value1": "1", "value2": "2"},
                        {"value1": "4", "value2": "3"},
                        {"value1": "1", "value2": "4"},
                        {"value1": "7", "value2": "5"}])
    df2 = pd.DataFrame([{"value1": "1", "value2": "2"},
                        {"value1": "4", "value2": "3"},
                        {"value1": "1", "value2": "4"},
                        {"value1": "7", "value2": "5"}])
    df3 = pd.DataFrame()
    # print(df[df["value1"] > df["value2"]])
    # print(df.index)
    # print(df.columns)
    # print(df1)
    # print(df2)
    print(df3.append(df2))


def test_insert():
    l = []
    l.insert(-1, 100)
    print(l)


def test_str_to_list():
    s = "[1, 2, 3]"
    print(type(eval(s)))
    for i in eval(s):
        print(i)

    l = [1, 2, 3]
    print(str(l))


def test_list():
    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
    print(l1.extend(l2))
    print(l1)

# def test_df2():
#     df = pd.DataFrame([{"id": "1", "age1": 1, "age2": 3},
#                        {"id": "2", "age1": 1, "age2": 3},
#                        {"id": "1", "age1": 3, "age2": 3},
#                        {"id": "2", "age1": 1, "age2": 3},
#                        {"id": "2", "age1": 1, "age2": 3},])
#     # print(df.groupby(["id"]))
#     # print(df["age2"].groupby([df["id"], df["age1"]]).sum())
#     return df["id"].value_counts("1")


def test_dict():
    d = {1: "a", 2: "b"}
    for i in d:
        print(d)


from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

# import numpy as np
# print(np.std([1, 2, 3]))

# se = pd.Series([1, 2, 3], index=["a", "b", "c"])
# print(se[-1])

def test_df2():
    df = pd.DataFrame([{"id": "1", "age1": "1", "age2": 3},
                       {"id": "2", "age1": "1", "age2": 3},
                       {"id": "1", "age1": "3", "age2": 3},
                       {"id": "2", "age1": "1", "age2": 3},
                       {"id": "2", "age1": "1", "age2": 3},])

    df1 = pd.DataFrame([{"age": 1, "name": "-1"},
                        {"age": 1, "name": "2"},
                        {"age": 1, "name": "-3"},
                        {"age": 1, "name": "4"}])

    df2 = pd.DataFrame([{"age": 1, "name": "0"},
                        {"age": 1, "name": "0"},
                        {"age": 1, "name": "0"},
                        {"age": 1, "name": "0"}])

    # print(df[df["age1"] == df["id"]])
    print(df1["name"])
    s = df1["name"].values <= df2["name"].values
    print(s)


from collections import OrderedDict
def test_od():
    od = OrderedDict()
    od["a"] = 1
    od["b"] = 2
    od["c"] = 3
    print(od.items())


def test_d():
    d = {" ": "123"}
    print(d)

def test_series():
    d_s = pd.Series([1, 2, 3, 4], index=list("aabc"))
    print(d_s[~d_s])
    # print(d_s.loc[d_s.index.duplicated(keep="first")])


def test_df5():
    df = pd.DataFrame([{"name": "小红", "age": "123"}])
    print(df["name"].tolist())
    print(df[df["name"] == "小红"])


def test_list1():
    l = []
    l.insert(-1, 'asdf')
    l.insert(0, 'first')
    print(l)


def get_s():
    se = pd.Series([6, 2, 3, 4, 5], index=list("abcde"))
    print(se[se.index < "c"].idxmax())


def test_list2():
    l = [1, 2]
    print(l[1:])

def test_list3():
    dt = {'index': ["10.0", 20, 30, 40], 'times': ['100', '200', '300', '400'], }
    df = pd.DataFrame(dt)
    df["index"] = df["index"].astype("int")
    print(df)

    # sum_int = df['index'].sum()
    # print(sum_int)


def test_s():
    series1 = pd.Series([i for i in range(10)], index=list("abcdefghij"))
    print(series1)
    print(series1.iloc[0])


def test_df6():
    df = pd.DataFrame(np.arange(20).reshape(5, 4), index=[1, 3, 4, 6, 8])
    print(df)
    df = df.reset_index(drop=True)
    print(df)

if __name__ == '__main__':
    test_list3()