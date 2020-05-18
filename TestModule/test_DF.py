import numpy as np
import pandas as pd

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


if __name__ == '__main__':
    calc_DF2()