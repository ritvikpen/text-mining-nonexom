import csv
import os

def analyzeFile(input, output):

    writer = csv.writer(output)

    for line in input:
        
        if ">" in line:
            label = line[1:]
        
        if "Identities" in line:
            if "Minus" not in line:
                dash_ind = 13
                if "/" in line:
                    dash_ind = line.index("/")
                data = line[11:dash_ind]
                row = [label,data]
                writer.writerow(row)
                label = ""
                data =  ""

def analyzeDirectory(directory, output):
    for file in os.listdir(directory):
        if(os.path.isfile(os.path.join(directory,file))):
            input_file = open(os.path.join(directory,file))
            output_file = open(output, "w", encoding='UTF8', newline='')
            analyzeFile(input_file, output_file)
        elif(os.path.isdir(os.path.join(directory,file))):
            analyzeDirectory(os.path.join(directory,file), output)

analyzeDirectory("analysis", "output_1.csv")