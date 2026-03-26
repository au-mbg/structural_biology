reinitialize

fetch 148L, async=0

hide all

select lysozyme, chain E

select cellwall, chain S

select sugar, chain A

select interactions, chain E and resi 104+70+11+145+106+26+35+166+114+137

deselect

show cartoon, lysozyme

color violetpurple, lysozyme

show sticks, cellwall or sugar

color green, cellwall

color skyblue, sugar

util.cnc cellwall or sugar

show sticks, interactions and (sidechain or name CA)

util.cnc interactions

set_view (\
     0.639346004,   -0.096025124,    0.762897432,\
    -0.083554909,    0.977618158,    0.193075478,\
    -0.764362395,   -0.187186167,    0.617013752,\
     0.000135008,   -0.000186734, -141.474243164,\
    8.011938095,   44.962886810,   35.425373077,\
    107.768066406,  175.175033569,  -20.000000000 )

scene overview, store

set_view (\
    -0.040578593, -0.737068772, -0.674594223,\
    -0.199193776, -0.655631781, 0.728331447,\
    -0.979117155, 0.163928986, -0.120214708,\
    0.000133797, 0.000027474, -56.231159210,\
    8.382658005, 51.830959320, 37.187347412,\
44.880794525, 67.567932129, -20.000000000 )

scene sugar, store

set_view (\

0.253545463, -0.673543334, -0.694297254,\
-0.243994251, -0.739075541, 0.627878845,\
-0.936041951, 0.010208250, -0.351730138,\
0.000015126, 0.000006150, -55.671298981,\
14.349269867, 52.413158417, 25.758239746,\
44.326564789, 67.013702393, -20.000000000 )

scene cellwall, store