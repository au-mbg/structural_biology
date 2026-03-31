# DNA GROOVE CODE
# Fetch your favourite DNA binding protein and color the DNA with this script.
# Colorblindfriendly: https://pymolwiki.org/index.php/Colorblindfriendly
# Written by Ebbe Sloth Andersen, 5/9-2020. Updated 13/9-2023.

select nts, resn DA+DT+DC+DG
hide everything, nts
show spheres, nts
color white, nts

# This link no longer works
# run https://github.com/Pymol-Scripts/Pymol-script-repo/raw/master/colorblindfriendly.py
# But this one does
run https://raw.githubusercontent.com/Pymol-Scripts/Pymol-script-repo/refs/heads/master/scripts/colorblindfriendly.py

# color AT major groove
select resn DT & name C7
color cb_bluish_green, sele
select resn DT & name O4
color cb_vermillion, sele
select resn DA & name N6
color cb_blue, sele
select resn DA & name N7
color cb_vermillion, sele

# color GC major groove
select resn DG & name O6
color cb_vermillion, sele
select resn DG & name N7
color cb_vermillion, sele
select resn DC & name N4
color cb_blue, sele

# color AT minor groove
select resn DT & name O2
color cb_vermillion, sele
select resn DA & name C2
color cb_yellow, sele
select resn DA & name N3
color cb_vermillion, sele

# color GC minor groove
select resn DC & name C5
color cb_yellow, sele
select resn DC & name O2
color cb_vermillion, sele
select resn DG & name N2
color cb_blue, sele
select resn DG & name N3
color cb_vermillion, sele

deselect