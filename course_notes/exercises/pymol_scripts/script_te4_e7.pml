reinitialize
bg_color white
fetch 1eft , async=0
create eftu , /1eft//A                       
hide everything

select nucleotide , /eftu///GNP or /eftu///MG
select sidechains , byres eftu within 4.0 of nucleotide
show sticks , nucleotide sidechains
color yellow , (nucleotide and name C\*)
center nucleotide

distance dist1 ,(nucleotide and name O6) , /eftu///174/OG
distance dist2 ,(nucleotide and name N1) , /eftu///139/OD1
distance dist3 ,(nucleotide and name N2) , /eftu///139/OD2
distance dist4 ,(nucleotide and name N7) , /eftu///136/ND2
distance dist5 ,(nucleotide and name O4') , /eftu///137/NZ


color blue , dist\*

set_view (\
     0.191412523,   -0.859790862,   -0.473412633,\
     0.693364501,   -0.222936183,    0.685232103,\
    -0.694701493,   -0.459409922,    0.553474486,\
     0.000000000,    0.000000000,  -64.049102783,\
     105.326667786,    6.069516182,   37.496429443,\
21.348415375,  106.749801636,  -20.000000000)