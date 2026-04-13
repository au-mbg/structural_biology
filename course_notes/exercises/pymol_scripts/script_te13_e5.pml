# Script til opgave 5. Antithrombin

fetch 1TB6, thrombin_antithrombin_complex, async=0

create heparin, /thrombin_antithrombin_complex/E

hide everything

show cartoon, /thrombin_antithrombin_complex/A+B+C

show sticks, heparin

color cyan, /thrombin_antithrombin_complex/A+B

color magenta, /thrombin_antithrombin_complex/C

util.cbaw heparin

set_view (\

-0.204501018, 0.901179492, 0.382169366,\

-0.261317968, 0.325990826, -0.908538342,\

-0.943340302, -0.285664320, 0.168829113,\

-0.000009358, -0.000028342, -322.122192383,\

44.415428162, 13.843706131, 13.705366135,\

244.209625244, 400.034790039, -20.000000000 )

scene F4, store

util.protein_vacuum_esp("thrombin_antithrombin_complex",mode=2,quiet=0,_self=cmd)

set_view (\

-0.204501018, 0.901179492, 0.382169366,\

-0.261317968, 0.325990826, -0.908538342,\

-0.943340302, -0.285664320, 0.168829113,\

-0.000009358, -0.000028342, -322.122192383,\

44.415428162, 13.843706131, 13.705366135,\

244.209625244, 400.034790039, -20.000000000 )

scene F5, store

hide everything

scene F4, recall

fetch 3SOR, XIa, async=0

remove solvent

align XIa, /thrombin_antithrombin_complex/B

hide cartoon, /thrombin_antithrombin_complex/A+B+C

util.protein_vacuum_esp("XIa",mode=2,quiet=0,_self=cmd)

set_view (\

0.400016606, 0.897881269, -0.183830276,\

-0.172334671, -0.123309925, -0.977286756,\

-0.900158465, 0.422612637, 0.105411202,\

0.000036344, -0.000114392, -204.280532837,\

49.031394958, 17.063432693, 28.728443146,\

161.061279297, 247.512329102, -20.000000000 )

scene F6, store