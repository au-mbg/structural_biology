reinit

# Get the Argonaute

fetch 3HK2, type=pdb1, async=0

remove solvent

# Ago domains

color red, chain C

color blue, chain D

hide cartoon, chain C+D

show sticks, chain C+D

# N domain

color cyan, chain A & resi 1-100

# Linker

color grey, chain A & resi 100-177

# PAZ domain

color purple, chain A & resi 177-272

# Linker

color grey, chain A & resi 272-338

# Mid domain

color orange, chain A & resi 338-464

# PIWI domain

color green, chain A & resi 464-685

set_view (\

0.123950958, 0.990234137, 0.063794814,\

-0.704351246, 0.133084893, -0.697266936,\

-0.698947906, 0.041492786, 0.713965237,\

0.000000000, 0.000000000, -259.055969238,\

17.825553894, -17.785488129, -42.222160339,\

204.241699219, 313.870239258, -20.000000000 )

scene F1, store, Ago domain structure.

# Show binding of 3'U

sele chain C

dist HB-DNA, sele, chain A, mode=2

hide labels

set_view (\

0.399974555, 0.880695522, -0.253753275,\

0.317198962, -0.392772764, -0.863202035,\

-0.859879613, 0.264764577, -0.436455190,\

-0.000459167, 0.000010028, -54.133724213,\

38.587257385, -17.265007019, -34.962413788,\

44.038654327, 64.241020203, -20.000000000 )

scene F2, store, Show binding of 3'U

# Show binding of RNA strand

sele chain D

dist HB-RNA, sele, chain A, mode=2

set_view (\

0.123950958, 0.990234137, 0.063794814,\

-0.704351246, 0.133084893, -0.697266936,\

-0.698947906, 0.041492786, 0.713965237,\

0.000000000, 0.000000000, -259.055969238,\

17.825553894, -17.785488129, -42.222160339,\

204.241699219, 313.870239258, -20.000000000 )

scene F3, store, 

# Show binding of RNA strand

scene F1