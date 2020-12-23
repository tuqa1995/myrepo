'''Write a program that reads the lines from flatland.txt and 
 only those lines that contain the word Triangles, Squares, Pentagons, Hexagons.
  Ignore the cases of the words'''


filename="flatland.txt"
myfile=open(filename,"r")
for line in myfile.readlines():
   
    for word in line.split():        
        if word.capitalize()=='Triangle' or word== 'Square'or  word=='Pentagon' or word== 'Hexagon':
            print(line)



            

