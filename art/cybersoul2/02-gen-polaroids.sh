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

convert -caption "$capt" \
          $x  -thumbnail 400x400 \
          -bordercolor Lavender -border 5x5   -density 144  \
          -gravity center  -pointsize 8   -background black \
          -polaroid 0   polaroids/${x/jpg/png}

done
