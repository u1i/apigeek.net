#cat > gallery.md <<EOF
#| | |
#| --- | --- |
#EOF

gen_capt()
{

	file=$1
	shift
	caption=$@

	convert -background white  -fill black -gravity South -font EB-Garamond-Bold -pointsize 18 -size 320x caption:"$caption" -bordercolor white -border 4 -bordercolor white -border 4 captions/$file


}

cp gallery.templ README.md

cat list.txt | xargs -n2 > /tmp/gen.txt

while read f
do
	set -f $f
	echo $1 and $2
	pic1=$1
	pic2=$2

	capt1=$(./get-caption-from-file.sh $pic1)
	capt2=$(./get-caption-from-file.sh $pic2)

	gen_capt $pic1 $capt1
	gen_capt $pic2 $capt2

	echo "| [![](${pic1})]($pic1) | [![](${pic2})]($pic2) |" >> README.md
	echo "| [![](captions/${pic1})]($pic1) | [![](captions/${pic2})]($pic2) |" >> README.md
	# echo "| $capt1 | $capt2 |" >> README.md
done < /tmp/gen.txt
