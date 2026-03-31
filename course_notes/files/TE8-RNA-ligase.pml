# This script shows details of RNA ligase class I
#
# Written by Ebbe Sloth Andersen, 14/9-2019 (extended 31/5-2022)

reinit

fetch 3HHN, type=pdb1, async=0 
fetch 3R1L, type=pdb1, async=0 
# 3HHN er postligation
# 3R1L is preligation complex with Mg

# Set the background color
bg_color white

# Focus on chain B and color stems like in Fig. 2 of Shechner-Bartel 2009
# https://www.science.org/doi/abs/10.1126/science.1174676

########################################################
# RPR view
########################################################
hide everything
show cartoon, 3HHN & chain C
show cartoon, 3R1L & (chain C or chain B)
color gray, all
color palegreen, resi 46-54+106-113
color forest, resi 55-59+65-70
color lightpink, resi 72-76+82-85
color purple, resi 86-105
color cyan, resi 5-10+115-121
color red, resi 35-39+77-81
color blue, resi -7-3+11-19
align 3HHN & chain C, (3R1L & (chain C or chain B))
set_view (\
     0.165754691,   -0.115665711,   -0.979361594,\
    -0.791867137,    0.576290488,   -0.202085555,\
     0.587771535,    0.809019387,    0.003931473,\
    -0.000065103,    0.000035211, -210.594436646,\
    -0.805380344,   37.034168243,   11.534556389,\
   135.342788696,  285.873565674,  -20.000000000 )
scene F1, store, RPR pre-ligation and post-ligation alignment - view as in Fig. 1 Shechner-2009 and 2011.
########################################################
# Active site view pre-ligation
########################################################
# Color residues around active site and show them as sticks
util.cbab resi \-1
util.cbam resi 1
util.cbab resi 30
util.cbay resi 47
util.cbao resi 71
hide everything, 3R1L
hide everything, 3HHN
show sticks, resi \-1+1+12+47+30+33+32+31+29+71 & 3R1L & (chain C or chain B)
show ribbon, 3R1L & (chain C or chain B)

# Label
set float_labels, on
set label_size, -1
label 3R1L & chain C & n. O4' & i. 1, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 29, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 30, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 31, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 32, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 33, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 47, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 71, "%s%s" % (resn, resi)
label 3R1L & chain C & n. O4' & i. 12, "%s%s" % (resn, resi)
label 3R1L & (chain C or chain B) & /3R1L//B/A`\-1/N7, "%s%s" % (resn, resi)

# Show polar contacts
select resi 1+47+30+33+32+31+29+71 & 3R1L & (chain C or chain B)
dist HB, sele, sele, mode=2
hide labels, HB

# show Mg ions
show spheres, /3R1L//C/MG`1019/MG
show spheres, /3R1L//C/MG`1020/MG
show spheres, /3R1L//C/MG`1041/MG
show spheres, /3R1L//C/MG`1035/MG
show spheres, /3R1L//C/MG`1034/MG
show spheres, /3R1L//C/MG`1042/MG

set_view (\
    -0.230300903,    0.677052796,    0.698971391,\
     0.483958840,   -0.543464482,    0.685881793,\
     0.844243705,    0.496233284,   -0.202506751,\
     0.000012338,   -0.000056431,  -86.062629700,\
   -11.206495285,   46.011726379,    5.941915989,\
   -94.917785645,  267.110656738,  -20.000000000 )

scene F2, store, RPR pre-ligation active site from Shechner-2011.
########################################################
# Active site view post-ligation
########################################################
hide everything, 3R1L
hide everything, 3HHN
show sticks, resi \-1+1+12+47+30+33+32+31+29+71 & chain C & 3HHN
show ribbon, 3HHN & chain C

# Label
set float_labels, on
set label_size, -1
label 3HHN & chain C & n. O4' & i. 1, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 30, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 47, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 71, "%s%s" % (resn, resi)


label 3HHN & chain C & n. O4' & i. 1, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 29, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 30, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 31, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 32, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 33, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 47, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 71, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. 12, "%s%s" % (resn, resi)
label 3HHN & chain C & n. O4' & i. \-1, "%s%s" % (resn, resi)

set label_position,(0,-1,0)

# Show polar contacts
hide everything, HB
select resi 1+47+30+33+32+31+29+71 & chain C & 3HHN
dist HB2, sele, sele, mode=2
hide labels, HB2

# show Mg ions
show spheres, /3HHN//C/MG`1019/MG
show spheres, /3HHN//C/MG`1020/MG
show spheres, /3HHN//C/MG`222/MG
show spheres, /3HHN//C/MG`123/MG

set_view (\
    -0.230300903,    0.677052796,    0.698971391,\
     0.483958840,   -0.543464482,    0.685881793,\
     0.844243705,    0.496233284,   -0.202506751,\
     0.000012338,   -0.000056431,  -86.062629700,\
   -11.206495285,   46.011726379,    5.941915989,\
   -94.917785645,  267.110656738,  -20.000000000 )

scene F3, store, RPR post-ligation active site from Shechner-2009.

scene F1