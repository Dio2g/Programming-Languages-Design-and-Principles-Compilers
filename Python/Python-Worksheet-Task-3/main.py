s  = "hello world"
myDict = {}
for ch in s:
  count = 0
  if ch in myDict:
    count = myDict[ch]
  myDict[ch] = count + 1
    
print(myDict)