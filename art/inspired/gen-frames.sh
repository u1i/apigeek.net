
frame[0]="1"
frame[1]="2"
frame[2]="4"
frame[3]="6"
frame[4]="8"

for x in *jpg
do
	echo $x
	rand=$[ $RANDOM % 5 ]

	convert $x -thumbnail 350x350 tmp/$x

	picframe -f ${frame[$rand]} -m 40 -b 1 tmp/$x tmp/tmp/$x
	convert tmp/tmp/$x -geometry 350x482! framed/$x
done
