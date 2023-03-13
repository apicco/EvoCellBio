#/bin/bash

files=`ls *fast/*txt`

i=0

for file in $files
do
	filename=`printf "180515-180824_MKYP0008_all/%03d.txt" $i`
	echo $filename
	cp $file $filename
	i=`echo "$i + 1" | bc`
done
