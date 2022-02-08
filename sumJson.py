import urllib.request, urllib.parse, urllib.error 
import json 

#read the json from url 
u = input("Enter an url: ") 
d = urllib.request.urlopen(u).read() 

#load the json data 
t = json.loads(d)

#to store count and sum of the numbers 
c = 0 
s = 0 

#loop trough the json data and count and sum the numbers  
for i in t["comments"]: 
    c += 1 
    s += int(i["count"])  
    
#print the result 
print("counter of numbers :", c) 
print("sum of numbers :", s) 
