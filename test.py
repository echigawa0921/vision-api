#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("hello world")
# print("aaaa")
# print("こんにちは・")


# 演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

# 変数
login_id = "L_size"
loiin_lenght = 5
login_times = 0

# 条件分岐と関係演算子
# == != < <= 
# if login_times = 0 :
#     print("ooi")
# elif login_times == 0:
#     print("nanimonai")
# else: 
#     print("sukunai")

# def unko_funbal(arg):
#     unko_status = arg

#     if(unko_status < 10):
#         return "mada_daijoubu"
#     else: 
#         return "yabai"

# # print(unko_funbal(12))

# unko_list = ["unko_small", "unko_big", "unko_medium"]
# # print(unko_list[0])

# # for 
# # for index in range(11):
# #     print(unko_funbal(index))

# for item in unko_list:
#     print(item)


# with
#open()

# with open('./pyenv.txt', 'r') as file:
#     print(file.mode)

# class

# class Card:
# 	def __init__(self, date, user_name):
# 		self.date = date
# 		self.user_name = user_name

# def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2020-01-01'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2020-01-03'
# user_name_b = 'kayoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

# import 
import math
print(math.pi)

import numpy

numpy_list = [3,1,5,10,2098,2211,3009,111]
print(numpy.sum(numpy_list))
