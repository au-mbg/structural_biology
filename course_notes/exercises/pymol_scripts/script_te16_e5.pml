reinit
fetch 1u19, async=0
create 1u19_acd, 1u19 and chain A+C+D
disable 1u19
hide all
show cartoon, 1u19_acd
util.rainbow("1u19_acd")
select ligands, 1u19_acd and (chain C+D or resn RET or resn PLM or resn HTG or resn HTO)
select ions, 1u19_acd and (elem HG or elem ZN)
select asn, 1u19_acd and (resi 2 or resi 15)
show sticks, ligands or asn
color skyblue, ligands
util.cnc ligands or asn
show sphere, ions
color grey50, ions
select none

set_view (\
    -0.720942974,   0.334131032,  -0.607121885,\
    -0.689282119,  -0.436299115,   0.578387737,\
    -0.071631059,   0.835463762,   0.544856608,\
    -0.000001192,   0.000056803,  -255.603088379,\
    39.933383942,   5.397409439,   8.031553268,\
    226.496871948,  284.712615967,-20.000000000)

scene F1, store

set_view (\
    -0.720942974, 0.334131032, -0.607121885,\
    -0.689282119, -0.436299115, 0.578387737,\
    -0.071631059, 0.835463762, 0.544856608,\
    0.000003095, 0.000004799, -88.668479919,\
    40.344326019, 1.528468490, 12.593762398,\
    75.946006775, 101.390907288, -20.000000000)

scene F2, store
select interact, byres (1u19_acd and chain A and resn RET around 4)
select retinol, 1u19_acd and resn RET
show sticks, interact or retinol
color skyblue, retinol
util.cnc interact or retinol
select none

fetch 3cap, async=0
create 3cap_acd, 3cap and chain A+C+D
disable 3cap
super 3cap_acd, 1u19_acd
orient 1u19_acd
