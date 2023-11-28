with open("table.txt", "r") as input: 
       
    with open("output_file.txt", "w") as output: 
          
        for line in input:
            for i in range(1,11): 
                line = int(line)
                output.write(f"{line} * {i} is {line*i}\n")
            output.write("\n") 
