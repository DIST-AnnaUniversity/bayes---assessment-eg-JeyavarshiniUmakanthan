# -*- coding: utf-8 -*-
"""bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13tz6HA6pdK767y3z5g_-7eXPDsajO6xC
"""

boys_having_book=5
boys_without_book=35
girls_having_book=20
girls_without_book=40
n=boys_having_book+boys_without_book+girls_having_book+girls_without_book
print(n)
p=(boys_having_book/(boys_having_book+girls_having_book)*((boys_having_book+girls_having_book)/n))/((boys_having_book+boys_without_book)/n)
print("probability of a student having book, given a boy=",round(p,2))