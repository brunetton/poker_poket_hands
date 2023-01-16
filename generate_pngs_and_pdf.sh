# Clean output dirs
rm -f pdf/* png/* svg/*

# First call translate script that will generate all translated svg files in svg/
./translate.py

# Then generate pdf and svg versions from those files
cd svg
for filename in *.svg; do
    echo $filename
    # PDF
    inkscape "$filename" --export-pdf="../pdf/${filename%.*}.pdf"
    # PNG (using group named "main" in svg file)
    png_filepath="../png/${filename%.*}.png"
    inkscape "$filename" --export-id="main" -d 200 --export-png="$png_filepath"
    # Add border using imagemagik
    convert "$png_filepath" -bordercolor white -border 15x10 "$png_filepath"
done
