## Script til opgave 1. Test dig selv i PyMOL-scripting

reinitialize

fetch 2q6h, LeuT1, async=0
fetch 2qju, LeuT2, async=0

hide all

# Spørgsmål 1

show cartoon, LeuT1
color lime, LeuT1

set_view (\
    -0.724445105,   -0.007380448,   -0.689293265,\
     0.413965195,   -0.804213703,   -0.426465273,\
    -0.551191866,   -0.594294727,    0.585663736,\
     0.000000000,    0.000000000, -250.922119141,\
    26.709741592,   30.848175049,   21.486454010,\
   204.134338379,  297.709991455,  -20.000000000 )

scene F1, store

# Spørgsmål 2

select na_ions, LeuT1 and resi 751+752
show sphere, na_ions
color violetpurple, na_ions

scene F2, store

# Spørgsmål 3

show sticks, LeuT1 and resi 112+179
util.cnc LeuT1

scene F3, store

# Spørgsmål 4

dist /LeuT1/A/A/ASN`179/ND2, /LeuT1/A/A/GLU`112/OE2

scene F4, store

# Spørgsmål 5

select site, LeuT1 and (na_ions around 6)
show sticks, site
util.cnc site
select none

scene F5, store

# Spørgsmål 6

show cartoon, LeuT2
align LeuT2, LeuT1

scene F6, store

# Spørgsmål 7

hide everything, LeuT1
spectrum b, blue_white_red, LeuT2

scene F7, store

# Spørgsmål 8

util.protein_vacuum_esp("LeuT2",mode=2,quiet=0,_self=cmd)

scene F8, store

