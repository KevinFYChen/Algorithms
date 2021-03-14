#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:00:10 2020

@author: kevinchen
"""
#This function implements a dynamic programming algorithm that solves the 
#longest common subsequence problem. Given 2 sequences, the function finds
#the longest common subsequence between the 2 and returns a list containing 2
#elements. The first element is a 2D array that records the length of LCS, the
#second element records the number of comparisons used while executing the 
#algorithm. The algorithm uses a bottom up approach which finds the solution 
#to a smaller subproblem first and then uses that solution to solve a bigger 
#subproblem.

def lcs_length(x,y):
    m=len(x)
    n=len(y)
    comp=0
    
    c=[[None for i in range(n+1)] for j in range (m+1)]
    
    for i in range(1,m+1):
        c[i][0]=0
    for j in range(n+1):
        c[0][j]=0
    
    #build the c[][] in a bottom-up fashion. c[i][j] records the length
    #of a LCS between 2 substrings x[1....i] and y[1...j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            #if the last characters of the 2 subsequences are the same, add  
            #the last element to the LCS
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                comp=comp+1
            #else, choose the longer LCS
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                comp=comp+2
            else:
                c[i][j]=c[i][j-1]
                comp=comp+3
    return c,comp