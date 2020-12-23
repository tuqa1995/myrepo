'''adapt the code above to count how often the word Flatland (with any capitalization) 
occurs in the first 5 lines. Print only the number of occurrences of that word.
 Once it works, remove the count so that you count the number of 
occurrences of the word in the text as a whole.'''

filename="flatland.txt"
myfile=open(filename,"r")
count=0
for line in myfile.readlines():
   
    for word in line.split():  
             
        if word=='Flatland':
            count=count+1
print(count)