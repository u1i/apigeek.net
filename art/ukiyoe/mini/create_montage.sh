# montage *jpg -tile 8x2 -geometry 100x100+3+3 out.png

montage $(cat list.txt) -tile 4x2 -geometry 200x200+3+3 out.png

montage $(cat list2.txt) -tile 4x2 -geometry 200x200+9+9 out2-tmp.png
convert -rotate 357 out2-tmp.png out2-tmp2.png
convert out2-tmp2.png -crop 824x412+10+10 -geometry 824x412 +repage out2.png

