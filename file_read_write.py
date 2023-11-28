i = open("table.txt", "r")
o = open("output_file.txt", "w") 
          
for line in i:
    line = int(line)
    o.write(f"{line} * {line} is {line*line}\n")
i.close()
o.close() 
