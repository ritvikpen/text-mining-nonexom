###-----------
cd /media/shraddha/MyPassport/NonExomics/Data/cancer/Experimental_validation/siRNAdesign/Parth18onwards/T18-84SiRNABLAST

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

#### Checking few cases where the number of mismatches in plus/Plus orientation is more than 16 - apart from target of interest.

for eachfile in T35CD.Ri.407915.13.1_8R0UJGDC016-Alignment.txt T24CD.Ri.407850.13.25_8A1HB23T01N-Alignment.txt T39CD.Ri.407921.13.17_8R85TJ1T01N-Alignment.txt T45CD.Ri.407974.13.24_8W2JHPB9016-Alignment.txt T45CD.Ri.407974.13.26_8W2KAX1A016-Alignment.txt T52CD.Ri.408001.13.7_8Z7SJ876016-Alignment.txt
do
	sed -e '1,/Alignments:/d' $eachfile > tempp_alignments.txt
	awk -F'\n' -v RS='>' -v ORS= '$1 !~  /Homo sapiens.*GRCh38/ {print RS $0}' tempp_alignments.txt > analysis/"$eachfile"_crosscheck
done