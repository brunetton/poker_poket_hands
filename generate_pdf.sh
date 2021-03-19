for filename in *.svg; do
    echo $filename
    inkscape "$filename" --export-pdf="pdf/${filename%.*}.pdf"
done
