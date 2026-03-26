reinitialize

fetch 2CPP, cytochrome, async=0

hide all

show cartoon, cytochrome

color skyblue, cytochrome

select heme, resn HEM

select camphor, resn CAM

select activesite, resi 87+96+297+247+244+295 and (sidechain or name CA)

show sticks, heme or camphor or activesite

color palegreen, camphor

color firebrick, heme

util.cnc

deselect

set_view (\

-0.990387917, -0.044599514, -0.130925521,\

-0.081105977, 0.954023838, 0.288548470,\

0.112036534, 0.296393573, -0.948471248,\

0.000098392, -0.000049323, -214.542510986,\

49.716114044, 42.711597443, 11.393342018,\

195.598297119, 233.486724854, -20.000000000 )

scene overview, store

set_view (\

-0.248216569, -0.520525157, -0.816970468,\

-0.620001614, 0.733363092, -0.278882563,\

0.744302213, 0.437299609, -0.504759789,\

0.000000000, 0.000000000, -54.386898041,\

45.986999512, 44.433998108, 12.432000160,\

35.442684174, 73.331115723, -20.000000000 )

scene active_site, store

scene overview, recall