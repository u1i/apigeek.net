#cat > gallery.md <<EOF
#| | |
#| --- | --- |
#EOF

def gen_capt()
{

	file=$1
	caption=$2

	convert -background white  -fill black -gravity South -font helvetica -pointsize 18 -size 320x   caption:"$caption" -bordercolor grey -border 10 captions/$2

bevelborder -s 8 -m inner -c 25 -b red -a 15 caption1.jpg cx.jpg

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

	gen_capt($pic1 $capt1)
	gen_capt($pic2 $capt2)

	echo "| [![](framed/${pic1})]($pic1) | [![](framed/${pic2})]($pic2) |" >> README.md
	echo "| $capt1 | $capt2 |" >> README.md
done < /tmp/gen.txt
