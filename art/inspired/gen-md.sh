#cat > gallery.md <<EOF
#| | |
#| --- | --- |
#EOF

cp gallery.templ gallery.md

cat list.txt | xargs -n2 > /tmp/gen.txt

while read f
do
	set -f $f
	echo $1 and $2
	pic1=$1
	pic2=$2

	echo "| [![](polaroids/${pic1/jpg/png})]($pic1) | [![](polaroids/${pic2/jpg/png})]($pic2) |" >> gallery.md
done < /tmp/gen.txt
