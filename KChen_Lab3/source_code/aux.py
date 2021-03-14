#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:52:23 2020

@author: kevinchen

This file contains all of the auxiliary functions used in the main function.
The purpose of writing these auxiliary function was to reduce the amount of
code in the main function so that it is more readable to the reader
"""
from lcs_length import lcs_length
from print_lcs import print_lcs

#This function compares each of the required input sequence to each other.
#It compares by pairs only and it prints out the LCS between each pair to the
#output file
def compare_S(S,outF):
    outF.write("required input sequences:\n")
    for i in range(len(S)):outF.write("{0}\n".format(S[i]))
    outF.write("\n\n")
    outF.write("comparing between the required input strings:\n")
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            outF.write("LCS between S{0} and S{1}:\n".format(i+1,j+1))
            c,comp=lcs_length(S[i],S[j])
            print_lcs(S[i],S[j],len(S[i]),len(S[j]),c,outF)
            outF.write("\n")
            report_stat(c,comp,outF,len(S[i]),len(S[j]))

#This function compares each of the test cases to each of the required 
#sequences. It compares by pairs only and it prints out the LCS between each
#pair to the output file
def compare_T(t,S,outF,num):
    for i in range(len(S)):
        outF.write("test case {0}: {1}\n".format(num,t))
        outF.write("S{0}: {1}\n".format(i+1,S[i]))
        outF.write("LCS: ")
        c,comp=lcs_length(t,S[i])
        print_lcs(t,S[i],len(t),len(S[i]),c,outF)
        outF.write("\n")
        report_stat(c,comp,outF,len(t),len(S[i]))

#This function prints the relevant statistics of each LCS computation to the
#output file
def report_stat(c,comp,outF,m,n):
    outF.write("length of LCS: {0}, # of "
               "comparisons: {1}\n\n".format(c[m][n],comp))