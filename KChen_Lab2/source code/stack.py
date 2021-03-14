#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:39:02 2020

@author: kevinchen

This file implements the stack class which is made to be embedded into the 
hash table. It does not require any additional space except for a few pointers
"""


class stack:
    def __init__(self):
        self.top=None
    
    #this function pushes a free slot from the hash table into the stack
    #it accepts the hashtable and the index of the free slot as its argument
    def push(self,array,index):
        if self.top is None or self.top==-1:
            array[index][2]=-1
        else:
            array[index][2]=self.top
        self.top=index
    def isEmpty(self):
        return (self.top is None or self.top==-1)
    
    #this function accepts the hash table as its argument and returns an 
    #available slot in the table as well as its index
    def pop(self,array):
        if self.isEmpty():
            return 
        index=self.top
        tmp=array[self.top]
        self.top=array[self.top][2]
        tmp[2]=None
        return tmp,index


    
    

        
        
        