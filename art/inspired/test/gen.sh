for x in *jpg
do

capt1=$(echo $x | sed "s/\.jpg//;" | tr "-" " " | tr "_" ":" | sed "s/:/: /;")

capt=""

for w in $capt1
do
	w2=`echo ${w:0:1} | tr  '[a-z]' '[A-Z]'`${w:1}
	capt="$capt $w2"
done

echo $x $capt

convert $x -thumbnail 400x400 tmp/${x/jpg/png}

picframe -f 1 -m 40 -b 1 tmp/${x/jpg/png} tmp2/${x/jpg/png}

convert tmp2/${x/jpg/png} -gravity South -pointsize 20 -font helvetica -annotate +0+35 "$capt" out/${x/jpg/png}

done
