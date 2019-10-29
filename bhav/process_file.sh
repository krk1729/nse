#NSE_PATH="/cygdrive/d/workShop/NSE/"
#SRC_PATH=$NSE_PATH"/src"
#DOWNLOADS_PATH=$NSE_PATH"/downloads"
#PROCESSED_FILES_PATH=$NSE_PATH"/processed"

mv cm*bhav.csv.zip ../downloads

cd ../downloads

find . -name "cm*bhav.csv.zip" -size -4k -delete

PGPASSWORD="postgres"

for file in `ls cm*bhav.csv.zip`
do 
   echo "Processing $file ..."
   time=`psql -h localhost -d postgres -p 5432 -u postgres -c "select now();"`

   #mv $file ../processed
done