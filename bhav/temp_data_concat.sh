cd ../downloads

for file in `ls cm*bhav.csv.zip`
do 
   zcat $file | tail +2 >> temp_data_file.csv
   if [ "$?" -eq "0" ]
   then
      mv $file ../zipped_files
   fi
done
