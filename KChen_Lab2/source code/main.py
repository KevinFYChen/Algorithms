#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:24:15 2020

@author: kevinchen

This file contains the main function of the script. It takes in an input file
containing records and insert them into a hash table that has 120 slots. It 
does so 11 times, each with a different hashing scheme. The main function 
prints the resulting hash tables to an output file. Input and output file must
be specified in the command line. 
"""
import sys,getopt
from aux import printList,hash_scheme

def main(argv):
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
  
    #first, put everything from the input file into a list. Only integers are
    #accepted, float numbers and other types of input are not accepted.
    i_list=[]
    for line in inF:
        line=line.strip()
        if len(line)==0:
            continue
        elif len(line.split())!=1:
            printList(i_list,outF)
            outF.write("invalid input: {0}\n".format(line))
            outF.write("please make sure that there is only 1 record "
                  "in each line")
            sys.exit()
        try:
            data=int(line)
        except:
            printList(i_list,outF)
            outF.write("invalid input: {0}".format(line))
            sys.exit()
        i_list.append(data)
    
    #print out the original input before the results
    outF.write("original input:\n")
    printList(i_list,outF) 
    #insert the records from the input file into 11 hash tables and print out
    #the results to the output file
    hash_scheme(i_list,"division",120,1, "linear",1,outF)
    hash_scheme(i_list,"division",120,1,"quadratic",2,outF)
    hash_scheme(i_list,"division",120,1,"chaining",3,outF)
    hash_scheme(i_list,"division",113,1,"linear",4,outF)
    hash_scheme(i_list,"division",113,1,"quadratic",5,outF)
    hash_scheme(i_list,"division",113,1,"chaining",6,outF)
    hash_scheme(i_list,"division",41,3,"linear",7,outF)
    hash_scheme(i_list,"division",41,3,"quadratic",8,outF)
    hash_scheme(i_list,"multiplication",120,1,"linear",9,outF)
    hash_scheme(i_list,"multiplication",120,1,"quadratic",10,outF)
    hash_scheme(i_list,"multiplication",120,1,"chaining",11,outF)
    
    inF.close()
    outF.close()

if __name__ == '__main__':
    main(sys.argv[1:])