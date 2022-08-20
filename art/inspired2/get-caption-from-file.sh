file=$1

capt1=$(echo $1 | sed "s/\.jpg//;" | tr "-" " " | tr "_" ":" | sed "s/:/: /;")

capt=""

for w in $capt1
do
	w2=`echo ${w:0:1} | tr  '[a-z]' '[A-Z]'`${w:1}
	capt="$capt $w2"
done

echo $capt | tr -d "\n"
