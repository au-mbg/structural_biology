reinitialize

fetch 1BL8, kchannel, async=0

hide all

select chainA, chain A
select chainB, chain B
select chainC, chain C
select chainD, chain D

color tv_blue, chainA
color tv_orange, chainB
color magenta, chainC
color yellow, chainD

show ribbon, kchannel

set_view (\
0.649728715, -0.607225955, 0.457305670,\
-0.557611287, 0.028152177, 0.829624295,\
-0.516643345, -0.794027805, -0.320305407,\
0.000000000, 0.000000000, -203.462997437,\
72.186561584, 26.599575043, 19.889984131,\
164.716903687, 242.209091187, -20.000000000 )

deselect

scene overview, store

select kions, elem K

show nb_spheres, kions

color palegreen, kions

select filter, resi 75-78

show sticks, filter

set_view (\
0.888863146, 0.193117291, -0.415483952,\
0.192342117, -0.980332971, -0.044177610,\
-0.415844947, -0.040646739, -0.908524752,\
0.000000000, 0.000000000, -61.653659821,\
67.867996216, 26.594999313, 9.017000198,\
45.950794220, 77.356529236, -20.000000000 )

deselect

scene filter, store

scene overview, recall