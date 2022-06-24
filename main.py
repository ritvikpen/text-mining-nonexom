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
            output_file = open(output, "a+", encoding='UTF8', newline='')
            analyzeFile(input_file, output_file)
        elif(os.path.isdir(os.path.join(directory,file))):
            analyzeDirectory(os.path.join(directory,file), output)

# note that the script will append to the output file parameter, so ensure
# that the file is either empty or only has relevant values within it before
# running this script on it
analyzeDirectory("analysis", "output_1.csv")