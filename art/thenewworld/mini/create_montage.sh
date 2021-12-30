# montage *jpg -tile 4x2 -geometry 100x100+3+3 out.png

montage $(cat list.txt) -tile 4x2 -geometry 200x200+3+3 out.png
