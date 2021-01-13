import matplotlib.pyplot as plt
myDictionary = {}
myStr = "hello world"
for ch in myStr:
  count = 0
  if ch in myDictionary:
    count = myDictionary[ch]
  myDictionary[ch] = count + 1
    
print(myDictionary)

labels = myDictionary.keys() 
heights = myDictionary.values()
left_edges = list(range(len(myDictionary)))
plt.xticks(left_edges , labels)
plt.title("Character Frequencies")
plt.xlabel("Character")
plt.ylabel("Frequency")
plt.grid(True)
bar_width = 1
plt.bar(left_edges, heights, bar_width, color=("r", "g", "b", "y", "k"))

plt.savefig("graph.png")