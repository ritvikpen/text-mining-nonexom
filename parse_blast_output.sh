
# make the analysis directory and generate the relevant .txt files
mkdir analysis
for eachfile in *-Alignment.txt
do
	sed -e '1,/Alignments:/d' $eachfile > tempp_alignments.txt
	awk -F'\n' -v RS='>' -v ORS= '$1 !~  /Homo sapiens.*GRCh38/ {print RS $0}' tempp_alignments.txt > analysis/tr_"$eachfile"
	awk -F'\n' -v RS='>' -v ORS= '$1 !~  /Homo sapiens.*GRCh38/ {print RS $0}' tempp_alignments.txt > tempp_output.txt
       grep -P 'Identities:\d+(/*)'  -o <(awk -F "," '{print $1}' <(grep -w "Plus/Plus" tempp_output.txt )) | tr "Identities:/" " " > tempp_identity.txt
       sed -i 's/           //' tempp_identity.txt 
       sort -k1,1nr tempp_identity.txt  > analysis/"$eachfile"_out    
    	rm tempp_*
done

# run the main.py file to generate the "_output" files
python3 main.py