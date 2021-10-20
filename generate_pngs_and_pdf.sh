for filename in *.svg; do
    echo $filename
    # PDF
    inkscape "$filename" --export-pdf="pdf/${filename%.*}.pdf"
    # PNG
    png_filepath="png/${filename%.*}.png"
    inkscape "$filename" --export-id="main" -d 200 --export-png="$png_filepath"
    # Add border using imagemagik
    convert "$png_filepath" -bordercolor white -border 15x10 "$png_filepath"
done
