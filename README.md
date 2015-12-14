##--- Day 14: Reindeer Olympics ---
####Problems are from http://adventofcode.com/ 

##Algorithm
1. Read inputs and store information name, flyingSpeed, flyingTime, restTime.
<br><br>
2. Read in the race time and store information as raceTime.
<br><br>
3. Calculate the distance each reindeer flew (using a for loop). 
<br><br>
```python
  a. For each reindeer i: 
      modAnswer = raceTime%(flyingTime[i]+restTime[i])
      divAnswer = raceTime/(flyingTime[i]+restTime[i])
      distReindeerFlew[i] = divAnswer * flyingTime[i]
      if(modAnswer==0)
        distReindeerFlew[i] = divAnswer * flyingTime[i] * flyingSpeed[i]
      else if(modAnswer<=flyingTime[i])
        distReindeerFlew[i] = (divAnswer * flyingTime[i] * flyingSpeed[i]) + (modAnswer* flyingSpeed[i])
      else
        distReindeerFlew[i] = (divAnswer * flyingTime[i] * flyingSpeed[i]) + (flyingTime[i]* flyingSpeed[i])
```
4. Distance of winning reindeer (O(n), where n is the number of reindeers in the contest)

```python
  a. initialise maxDis = 0
  b. For each reindeer i
        if(maxDis < distReindeerFlew[i])
          maxDis = distReindeerFlew[i]
  c. return maxDis
```
          
  
        
        
      

      

