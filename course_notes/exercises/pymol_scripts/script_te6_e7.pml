# Script til opgave 7. Arc repressor

reinit 

fetch 1BDT, type=pdb1, async=0 

remove solvent 

set_view (\

0.729630232, -0.663575828, -0.165245384,\

0.033471450, 0.276007086, -0.960573792,\

0.683021665, 0.695331573, 0.223593742,\

0.000000000, 0.000000000, -188.640228271,\

43.895526886, -2.066005707, 25.748359680,\

148.725402832, 228.555053711, -20.000000000 )

scene F1, store

color purple, ss h & chain A+B+C+D
color yellow, ss s & chain A+B+C+D
color cyan, ss l+"" & chain A+B+C+D

scene F2, store

dist DIST, name CB & resi 11 & chain A, name CB & resi 11 & chain C, mode=0

scene F3, store

hide everything, DIST

show sticks, chain E+F

util.cbaw chain E+F

show sticks, resi 8-14 and chain A+B+C+D
util.cbac resi 8-14 and chain A+B+C+D

dist H-bond, resi 8-14 and chain A+B+C+D, chain E+F, mode=2

hide labels

scene F4, store