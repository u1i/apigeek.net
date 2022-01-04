for x in *jpg
do
	echo $x
	picframe -f 1 -m 80 -b 1 $x framed/$x
done
