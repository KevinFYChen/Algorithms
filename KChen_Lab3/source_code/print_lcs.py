#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:59:19 2020

@author: kevinchen
"""
#This function prints out the longest common subsequence (LCS) between 2 
#sequences. It takes in 2 sequences X and Y and a 2D array c[][] that records 
#the length of the LCS between each substring of X and Y. It prints out the 
#LCS between X and Y. 
def print_lcs(x,y,i,j,c,outF):
    if i==0 or j==0:
        return 
    
    #if the last character of x and y are identical, print out the character
    if x[i-1]==y[j-1]:
        print_lcs(x,y,i-1,j-1,c,outF)
        outF.write(x[i-1])
    #if x[i-1] != y[j-1], choose the LCS that is the longest
    elif c[i-1][j]>=c[i][j-1]:
        print_lcs(x,y,i-1,j,c,outF)
    else:
        print_lcs(x,y,i,j-1,c,outF)
    
    