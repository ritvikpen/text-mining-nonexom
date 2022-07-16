# About
This code will look through the BLAST alignment output files and generate a final ".tsv" file that contains the list of transcripts with over 16 bp matches within the BLAST query. 

# Running Instructions
The main.py, parse_blast_output.sh, and run.sh files all need to placed within the parent target-seq directory (the parent directory to each of the "BLAST RESULTS" directories). 

Running the `run.sh` file will then result in the `main.py` and `parse_blast_output.sh` files being copied into each of the "BLAST RESULTS" directories and the `parse_blast_output.sh` being run to generate the final "_output.tsv" file. 