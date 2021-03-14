#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:48:34 2020

@author: kevinchen

This file contains all of the auxiliary functions used in the main function
It contains the following functions:
    printList
    hash_scheme
    printHash
"""
from hashtable import hashtable

#This function prints out the original records from the input file. It prints 
#out 5 records in each line.
def printList(i_list,outF):
    count=1
    size=len(i_list)
    for i in range(size):
        if count<5 and i is not size-1:
            outF.write("{0}, ".format(i_list[i]))
            count+=1
        else:
            outF.write("{0}\n".format(i_list[i]))
            count=1

#This function implements a routine that hashes all of the records from the 
#input file to the hash table. h_scheme tells the function whether 
#it should use division or multiplcation, m is the modulo number in division 
#and also the table size value in multiplication. c_scheme tells the function 
#which collision handling method to use. All results are printed to the 
#output file. Records that could not be inserted are also printed to the 
#output file
def hash_scheme(l, h_scheme, m, bucket, c_scheme,scheme_num,outF):
    htable=hashtable(bucket=bucket)
    index=None
    for i in range(len(l)):
        if h_scheme=="division":
            hv=htable.division(l[i],m)
        elif h_scheme=="multiplication":
            hv=htable.multiplication(l[i],m)
        if bucket==1:
            j=htable.insert(l[i],hv,c_scheme,120)
        elif bucket>1:
            j=htable.insert(l[i],hv,c_scheme,40)
        if type(j)==str:
            index=i
            break
    printHash(outF,htable,h_scheme,m,bucket,c_scheme,scheme_num)
    if index is not None:
        outF.write("{0}\n".format(j))
        outF.write("items unable to be stored in the hash table:\n")
        printList(l[index:],outF)

#This function prints the hash table to the specified output file along with
#all of the relevant statistics. If the bucket size is 1, then the 
#function prints out 5 records in each line. If the bucket size is 3, then 
#the function prints out 3 records in each line.
def printHash(outF,htable,h_scheme,modulo,bucket,c_scheme,scheme_num) :
    alpha=htable.n/len(htable.array)
    if h_scheme=="division":
        outF.write("\nscheme {0} (division) - modulo: {1},".format(scheme_num,
            modulo)+" bucket size: {0}, {1}\n".format(bucket,c_scheme))
    elif h_scheme=="multiplication":
        outF.write("\nscheme {0} (multiplication) - bucket size: {1}, ".format
                   (scheme_num,bucket) + "{0}\n".format(c_scheme))
    outF.write("# of collisions: {0}, # of comparisons: {1}, ".format(
               htable.collisions,htable.comparisons) + 
               "records inserted: {0}, ".format(htable.n)+
               "load factor: {0}\n".format(alpha))
    if bucket==1:
        count=1
        size=len(htable.array)
        for i in htable.array:
            if count<5 and i is not size-1:
                outF.write("{0},  ".format(i[0]))
                count+=1
            else:
                outF.write("{0}\n".format(i[0]))
                count=1
    elif bucket>1:
        for i in htable.array:
            outF.write("{0}\n".format(i))

