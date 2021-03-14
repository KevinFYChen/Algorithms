#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:27:10 2020

@author: kevinchen

This program takes sequences from an input file and outputs the longest common
subsequence between the input sequences. The input file should follow the 
following format:
S1=sequence 1
S2=sequence 2
S3=sequence 3
S4=sequence 4

sequence 1
sequence 2
.
.

The required input strings must be the first 4 strings in the input file and
prefixed with 'S1/S2/S3/S4 ='. The test cases follows the required strings and 
have no prefixes. All sequences must be in one of the 4 bases {A,T,C,G}. Upper
or lower case does not matter

Besides from the main function, this program utilizes the following functions:
    lcs_length
    print_lcs
    compare_T
    compare_S

lcs_length and print_lcs computes and prints the LCS between 2 sequences. 
compre_T and compare_S are 2 auxiliary functions that compute the LCS between 
sequences from the input file
"""
import sys,getopt
import re
from aux import compare_S,compare_T

def main(argv):
    num=0
    try:
        opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
        #specifying how this program should be executed 
        print ("main.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
      
    for opt, arg in opts:
        if opt == '-h':
            print ("main.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i"):
            inputfile = arg
        elif opt in ("-o"):
            outputfile = arg
    
    inF=open(inputfile,"r")
    outF=open(outputfile,"w")
    required_input=[]
    for line in inF:
        line=line.strip()
        #skip empty lines
        if len(line)==0:
            continue
        #if a "S1/S2/S3/S4 =" prefix is identified then the sequence is a 
        #required sequence
        m=re.search("^S\d\s*=",line)
        if m:
            tmp=re.split("=",line)
            seq=tmp[1].strip()
        else:
                seq=line
        #check if any characters other than ATCG is in the sequence
        m2=re.search("[^atcgATCG]",seq)
        if m2:
            if len(required_input) < 4:
                for i in required_input: outF.write("{0}\n".format(i))
            outF.write("error sequence: {0}\n".format(seq))
            outF.write("sequence contains character(s) that is not "
                       "A,T,C or G")
            return
        #make all sequence appear in upper case for consistency
        seq=seq.upper()
        if m:
            required_input.append(seq)
            #if all 4 required inputs are recorded then we compare each of the
            #required input with the others. 
            if len(required_input)==4:
                compare_S(required_input,outF)
                outF.write("\ncomparing the test cases to each of "
                           "the required input strings:\n\n")
        else:
            #this deals with the error case where a test case appears before 
            #a required input in the input file
            if len(required_input) < 4:
                for i in required_input: outF.write("{0}\n".format(i))
                outF.write("error: not all of the 4 required strings are "
                           "detected, please make sure the required strings "
                           "are prefixed with 'S1/S2/S3/S4 =' and please make"
                           " sure that they are the first 4 lines in the "
                           "input file")
                return
            num+=1
            compare_T(seq,required_input,outF,num)
            
    inF.close()
    outF.close()


        
if __name__ == '__main__':
    main(sys.argv[1:])
    
    
    
    
    