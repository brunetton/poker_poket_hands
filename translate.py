#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate translated versions of "poker hands.svg" using sed in svg/ dir
"""

import subprocess
from pathlib import Path

import yaml

# Read translations.yaml file
try:
    translations = yaml.load(Path("translations.yaml").read_text(), Loader=yaml.BaseLoader)
except yaml.parser.ParserError as e:
    print(e)
    exit("Error decoding translations.yaml")

# Create output directory (svg/)
svg_path = Path('svg/')
svg_path.mkdir(parents=False, exist_ok=True)

# Copy English version in svg/
english_version_path = Path("poker hands.svg")
subprocess.Popen(f"cp '{english_version_path}' svg/", shell=True)

# Generate svg files (in svg/ dir)
for lang_name, lang_translations in translations.items():
    print(f"-> {lang_name}")
    # generate array of sed commands for this language. Example: ['s/>High card</>Carte Haute</I', 's/>Pair</>Paire</I']
    sed_commands = [f"s/>{ori}</>{translated}</I" for ori, translated in lang_translations.items()]
    # call sed. Example: "sed 's/>High card</>Carte Haute</I;s/>Pair</>Paire</I' 'poker hands.svg' > 'svg/poker hands - Fr.svg'"
    sed_command = f"sed '{';'.join(sed_commands)}' '{english_version_path}' > '{svg_path}/poker hands - {lang_name.capitalize()}.svg'"
    subprocess.Popen(sed_command, shell=True)

print("\n=> End")
