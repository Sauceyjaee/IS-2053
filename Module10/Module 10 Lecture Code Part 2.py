# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:29:15 2022

@author: iburr
"""
import random

class Coin:
    
    def __init__(self):
        self.__sideup = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    def get_sideup(self):
        return self.__sideup
    
    def __str__(self):
        return f'The current state of the coin is {self.__sideup}'
    
def main():
    
    my_coin = Coin()
    my_coin2 = Coin()
    
    print("This side is up", my_coin.get_sideup())
    
    for count in range(10):
        
        my_coin.toss()
        #my_coin.sideup = 'Heads'
        print(my_coin.get_sideup())
     
    
    print(my_coin)
    print('\n')
    
    for count in range(10):
        
        my_coin2.toss()
        print(my_coin2.get_sideup())

    print(my_coin2)

if __name__ == "__main__":
    
    main()