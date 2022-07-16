import csv
import os
import numpy as np

'''
The analyzeFile() method takes in a the relevant input and 
output file parameters. The method looks through the input
file and identifies relevant transcripts and stores the name
and number of matches.
'''
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

'''
The analyzeDirectory() method takes in a directory and runs the 
analyzeFile() methood on every .txt file within the directory. 
'''
def analyzeDirectory(directory):
    for file in os.listdir(directory):
        if "txt_out" not in file:
            output = file[0:(len(file) - 4)] + "_output.csv"
            if(os.path.isfile(os.path.join(directory,file))):
                input_file = open(os.path.join(directory,file))
                output_file = open(output, "a+", encoding='UTF8', newline='')
                analyzeFile(input_file, output_file)
            elif(os.path.isdir(os.path.join(directory,file))):
                analyzeDirectory(os.path.join(directory,file))

# note that the script will append to the output file parameter, so ensure
# that the file is either empty or only has relevant values within it before
# running this script on it
analyzeDirectory("analysis")

'''
The finalAnalysis() method looks through each of the "_output.csv" files
generated in the previously called analyzeDirectory() method and identifies
relevant transcripts with values over 16 and stores them in a final 
"_output.tsv" file.
'''
def finalAnalysis():
    
    path = os.getcwd()
    path_name = path.split("/")[-1].split("_")[0]

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if "csv" in f:
            desArr = f.split("_")
            desID = desArr[1][desArr[1].index("C"):]
            input = open(f)
            input_file = csv.reader(input, delimiter=",")
            transcripts = []
            numbers = []
            for line in input_file:
                # conditional checks to make sure value is over 16 and not a duplicate
                if((int(line[1]) >= 16) and (line[0].strip("\n") not in transcripts)):
                    transcripts.append(line[0].strip("\n"))
                    numbers.append(line[1])

            # write to the output file, making sure to append instead of overwrite
            with open(path_name + '_output.tsv', 'a+', newline='') as f_output:
                for i in range(len(transcripts)):
                    data = [desID, transcripts[i], numbers[i]]
                    tsv_output = csv.writer(f_output, delimiter='\t')
                    tsv_output.writerow(data)

finalAnalysis()