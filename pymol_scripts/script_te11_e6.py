from pymol import cmd

@cmd.extend
def count_amino_acid(amino_acid):
    amino_acid_space={"amino_acids":[]}
    cmd.iterate("name CA and resn {}".format(amino_acid), "amino_acids.append(resi)",space=amino_acid_space)
    print(len(amino_acid_space["amino_acids"]))
    return 