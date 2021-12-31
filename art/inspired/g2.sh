#cat > gallery.md <<EOF
#| | |
#| --- | --- |
#EOF

cp gallery.templ g2-README.md

cat list.txt | xargs -n2 > /tmp/gen.txt

while read f
do
	set -f $f
	echo $1 and $2
	pic1=$1
	pic2=$2

	out1=""
	out2=""

	for pic in $pic1 $pic2
	do
		capt1=$(echo $pic | sed "s/\.jpg//;" | tr "-" " " | tr "_" ":" | sed "s/:/: /;")
		
		capt=""
		
		for w in $capt1
		do
			w2=`echo ${w:0:1} | tr  '[a-z]' '[A-Z]'`${w:1}
			capt="$capt $w2"
		done

		echo $pic $capt

		out=g2-${pic/jpg/md}
		echo "#$capt\n" > $out
		echo "![]($pic)" >> $out

		if [ "$out1" = "" ]
		then
			out1=$out
		else
			out2=$out
		fi
	done

	echo out1 $out1 out2 $out2
	echo "| [![](polaroids/${pic1/jpg/png})]($out1) | [![](polaroids/${pic2/jpg/png})]($out2) |" >> g2-README.md
done < /tmp/gen.txt
