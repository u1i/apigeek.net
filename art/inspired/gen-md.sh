#cat > gallery.md <<EOF
#| | |
#| --- | --- |
#EOF

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

	echo "| [![](framed/${pic1})]($pic1) | [![](framed/${pic2})]($pic2) |" >> README.md
	echo "| $capt1 | $capt2 |" >> README.md
done < /tmp/gen.txt
