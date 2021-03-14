#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:11:46 2020

@author: kevinchen

This file implements the hash table class. It includes class methods insert, 
division, multiplication, chaining, probing and initiateStack. The function
initiateStack is used to facilitate chaining. This class utilizes a stack
object which is implemented in another file. The stack is used to keep track
of the free space in the table
"""
from stack import stack
import math

class hashtable:
    def __init__(self,length=120,bucket=1):
        if bucket==1:
            self.array=[[None for i in range(3)] for j in range (length)]
            self.free=stack()
            self.initiateStack()
        else:
            new_length=int(length/bucket)
            self.array=[[None for i in range(bucket)]for j in 
                         range(new_length)]
        self.bucket=bucket
        self.collisions=0
        self.n=0
        self.comparisons=0
    
    #When the hashtable object is instantiated, we initially put all empty
    #slots into a stack object to keep track of the free slots. This function
    #is written to facilitate chaining
    def initiateStack(self):
        for i in range(len(self.array)):
            self.free.push(self.array,i)
    
    #This method is how the division and multiplication scheme is implemented.
    #It accepts an argument h_value which is the hash value calculated from 
    #either the multiplication or the division method. c_scheme tells the
    #function which collision handling method to use when self.array[h_value]
    #is full. probe_m is the "m" value used in the probing function which can
    #either be 120 or 40, depending on the bucket size. This function outputs
    #the index of the slot at which the record is inserted. If the table is
    #full, the function will return a string that says it's full.
    def insert(self, data,h_value,c_scheme,probe_m):
        if self.bucket==1:
            self.comparisons+=1
            if self.array[h_value][0] is None:
                self.array[h_value][0]=data
                self.n+=1
                return h_value
        elif self.bucket>1:
            target=self.array[h_value]
            for i in range(len(target)):
                self.comparisons+=1
                if target[i] is None:
                    target[i]=data
                    self.n+=1
                    return h_value
        self.collisions+=1
        if c_scheme=="chaining":
            j=self.chaining(self.array[h_value],h_value)
        elif c_scheme=="linear":
            j=self.probing(h_value=h_value,c1=1,c2=0,m=probe_m)
        elif c_scheme=="quadratic":
            j=self.probing(h_value=h_value,c1=0.5,c2=0.5,m=probe_m)
        if type(j)==int:
            original=self.comparisons
            self.insert(data,j,c_scheme,probe_m)
            self.comparisons=original
        return j
    
    #this function implements the division method of probing. A hash value of 
    #40 when the table size is 40 will be re-hashed to 0
    def division(self,data,m):
        r=(data % m)
        if r==40 and len(self.array)==40:
            r=0
        return r
    
    #this function implements the multiplication method of probing
    def multiplication(self,data,m):
        A=(math.sqrt(5)-1)/2
        hv=math.floor(m*((data*A)%1))
        return hv
    
    #this function implements chaining
    def chaining(self,current,h_value):
        while current[0] is not None and current[1] is not None:
            #find the end of the chain
            current=self.array[current[1]] 
            self.comparisons+=1
        while True:
            if self.free.isEmpty():
                return "error: hash table is full"
            else:
                tmp,j=self.free.pop(self.array)
            #some of the slots in the stack may be full due to primary hashing
            #so we need to check to see if the popped slot is available
            if tmp[0] is None:
                current[1]=j
                break
        return j
    
    #this function is used to implement both linear and quadratic probing. In
    #the case of linear probing, c1=1 and c2=0, in the case of quadratic 
    #probing, c1 and c2 equal 0.5. m can either be 120 of 40 depending on the
    #bucket size
    def probing(self,h_value,c1,c2,m):
        #since we have already tested i=0 in the insert function, we start 
        #with i=1
        i=1     
        while i<m:
            j=int(h_value+(c1*i)+(c2*(i**2)))%m
            if self.bucket==1:
                self.comparisons+=1
                if self.array[j][0] is None:
                    return j
            elif self.bucket>1:
                target=self.array[j]
                for k in range(len(target)):
                    self.comparisons+=1
                    if target[k] is None:
                        return j
            i+=1
            self.collisions+=1
        if c1==1 and c2==0:
            return "error: hash table is full"
        else:
            str1="error: quadratic probing cannot find any more empty slots "
            str2="within {0} probes".format(m)
            return str1 +str2
                  
        
        
        
        
    
        
