for x in *png
do
	echo *png
	convert $x -crop 1024x1000+0+0 ${x/png/jpg}
done
