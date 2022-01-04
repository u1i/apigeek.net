for x in *jpg
do
	echo $x

	convert $x -thumbnail 400x400 tmp/$x

	picframe -f 1 -m 40 -b 1 tmp/$x framed/$x
done
