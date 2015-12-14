#Written by : Tan Si Ling
#Date : 14 Dec 2015

import numpy as np
import scipy as sp

#Go to the correct directory 
#import os
#os.chdir('/Users/Siling/Desktop/AdventOfCode')
#print os.getcwd()
#print os.listdir(".")


#Load text and seperate them with \t 
# Type in the file that you want to read
data = np.loadtxt('input.txt', dtype = np.str, delimiter='\t')

#initialization
flyingSpeed = np.zeros(len(data))
flyingTime = np.zeros(len(data))
restTime = np.zeros(len(data))
distReindeerFlew = np.zeros(len(data))
raceTime = 2503.0   #assume in sec
modAnswer = 0
divAnswer = 0
maxDis = 0

#load the data into arrays
for i in range (len(data)):
    stringData = data[i]
    sliceData = stringData.split()
    flyingSpeed[i] = sliceData[3]   #assume in km/s
    flyingTime[i] = sliceData[6]    #assume in sec
    restTime[i] = sliceData[13]     #assume in sec
    
    
for i in range (len(data)):
  modAnswer = raceTime%(flyingTime[i]+restTime[i])
  divAnswer = int(raceTime/(flyingTime[i]+restTime[i]))
    
  #print flyingTime[i], restTime[i], modAnswer, divAnswer
  distReindeerFlew[i] = divAnswer * flyingTime[i]
  if (modAnswer==0):
    distReindeerFlew[i] = divAnswer * flyingTime[i] * flyingSpeed[i]
  elif(modAnswer<=flyingTime[i]):
    distReindeerFlew[i] = (divAnswer * flyingTime[i] * flyingSpeed[i]) + (modAnswer* flyingSpeed[i])
  else:
    distReindeerFlew[i] = (divAnswer * flyingTime[i] * flyingSpeed[i]) + (flyingTime[i]* flyingSpeed[i])
 
# finding which reindeer flew the furthest
for j in range (len(data)):
    if(maxDis < distReindeerFlew[j]):
        maxDis = distReindeerFlew[j]

# print out the console the maximum dist
print maxDis
    
