# remove the spaces from all directories
for f in *\ * 
do 
    mv "$f" "${f// /_}"
done

# move the parse_blast_output.sh and main.py files to each
# directory and then run the parse_blast_output.sh file
for dir in */ 
do
    echo $dir
    cp parse_blast_output.sh $dir
    cp main.py $dir
    cd $dir
    bash parse_blast_output.sh
    cd ..
done 