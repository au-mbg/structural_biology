reinitialize

bg_color white
set opaque_background, off
run colCons.py

fetch 1mbd
color_cons('1mbd','globin-aln-fasta.txt',1,1,0.5,1.0,'rain','yellow','red','BLOSUM62',True)

reinit
fetch 1hbb 1gdj 1mbd, async=0
remove solvent
remove not(chain A)
align 1hbb, 1mbd
align 1gdj, 1mbd
reset
color_cons('1hbb','globin-aln-fasta.txt',3,1,0.5,1.0,'rain','yellow','red','BLOSUM62',True)
color_cons('1mbd','globin-aln-fasta.txt',1,1,0.5,1.0,'rain','yellow','red','BLOSUM62',True)
color_cons('1gdj','globin-aln-fasta.txt',2,1,0.5,1.0,'rain','yellow','red','BLOSUM62',True)