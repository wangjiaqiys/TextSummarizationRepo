# _*_ coding:utf-8 _*_
# Created by JiaQi at 08/10/2020

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
    return data