#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:34:13 2018

@author: Nikie Jo Deocampo
"""
import json
import csv
from nltk.tokenize import word_tokenize
import string
import re
import time
import pandas as pd



tweets_data = []
x = []
y = []
k = []
some_milby = []
print("===========================")
print("Starting Preprocess Function")
print("=========================== \n\n")

def getdata(dataurl):
    print("===========================")
    print("Retrieving TXT File")
    tweets_data_path = dataurl
    tweets_file = open(tweets_data_path,"r", encoding = 'cp850')
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    print("===========================")
    print("Retrieving Successfull")
    print("=========================== \n \n")
    time.sleep(3)
    processdata()


def processdata():
    print("===========================")
    print("Recovering Data Teets")
    print("===========================")
    time.sleep(1)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    for i in range(len(tweets_data)):
        q = tweets_data[i]['tweet']
        o = str(tweets_data[i]['id'])
        q = RE_EMOJI.sub(r'', q)
        i = q.translate(str.maketrans('','',string.punctuation))
        x.append(i)
        k.append(o)
    print("===========================")
    print("Data Tweets Recovered")
    print("===========================\n\n")
    
    
    
def readdict(dataurl):
    print("===========================")
    print("Reading Dictionary")
    print("===========================")  
    with open(dataurl) as csvfile:
      reader = csv.reader(csvfile, delimiter='\t')
      for row in reader:
          i = []
          i.append(row[0])
          i.append(row[1])
          y.append(i)
                  
    print("===========================")
    print("Dictionary Preparation Done")
    print("===========================\n\n")  
    addpolarity()
    

def addpolarity():  
    start_time = time.time()
    counter = 0
    print("===========================")
    print("Processing please wait...")
    print("===========================\n\n")
    for j in x:
            tweet_token = j
            token = word_tokenize(tweet_token)
            sumnum = 0
            sum_word = 0
            sum_more = 0
            for t in token:
                for d in y:
                    if t == d[0]:
                        sentiment = d[1]
                        if sentiment == "positif":
                            sumnum += 1
                            sum_word += 1
                        elif sentiment == "negatif":
                            sumnum += -1
                            sum_word += 1
                        else:
                            sumnum += 0
                            sum_word += 1
                        break

            if sum_word != 0.0:
                sum_more = sumnum / sum_word
                if sum_word != 0.0:
                    sum_more = sumnum / sum_word
                if sum_more >= 0.2:
                    sum_more = 1
                elif (sum_more < 0.2) and (sum_more > -0.5):
                    sum_more = 0
                elif sum_more <= -0.5:
                    sum_more = -1
            sum_var = []    
            varid = k[counter]
            sum_var.append(varid)
            sum_var.append(sum_more)
            some_milby.append(sum_var)
            # print (sum_var)
            counter += 1
            
    print("Processing time: ", round((time.time() - start_time),8), "Seconds \n\n")
    
    time.sleep(1)
        
    print("===========================")
    print("Processing Finish")
    print("===========================")
    
    
    savetoxlsx()
    
def savetoxlsx():
    df = pd.DataFrame(some_milby)
    df.to_excel('processed_data/outputBaru1.xlsx', header=("id","sentiment"), index=False)
    
    print("===========================")
    print("Data Saved!")
    print("===========================") 

def runall():
    getdata('data/vaksinTWEET.json')
    readdict('data/dicTerbaru.tsv')
    


runall()
# import nltk
# nltk.download('punkt')