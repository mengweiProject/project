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


if __name__ == '__main__':
    # d = collections.OrderedDict({"a": 1})
    create_df()