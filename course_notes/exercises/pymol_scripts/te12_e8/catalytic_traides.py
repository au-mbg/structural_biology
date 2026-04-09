from pymol import cmd


@cmd.extend
def SP_catalytic_triad_finder(selection="all"):
    aaspace = {"asplist": [], "hislist": [], "serlist": []}
    cmd.iterate(
        "resn Asp and name CA and ({})".format(selection),
        "asplist.append(resi)",
        space=aaspace,
    )
    cmd.iterate(
        "resn His and name CA and ({})".format(selection),
        "hislist.append(resi)",
        space=aaspace,
    )
    cmd.iterate(
        "resn Ser and name CA and ({})".format(selection),
        "serlist.append(resi)",
        space=aaspace,
    )
    distspace = {"asphisdist": [], "finallist": []}
    maxaadist = 7

    for i in aaspace["asplist"]:
        for j in aaspace["hislist"]:
            try:
                asptohis = cmd.get_distance(
                    atom1="(resi {} and name CG and {})".format(i, selection),
                    atom2="(resi {} and name NE2 and {})".format(j, selection),
                )
            except:
                continue
            if asptohis < maxaadist:
                distspace["asphisdist"].append([i, j])

    accu = -1
    for i in distspace["asphisdist"]:
        accu += 1
        for j in aaspace["serlist"]:
            try:
                asptoser = cmd.get_distance(
                    atom1="(resi {} and name CG and {})".format(i[0], selection),
                    atom2="(resi {} and name OG and {})".format(j, selection),
                )
                histoser = cmd.get_distance(
                    atom1="(resi {} and name NE2 and {})".format(i[1], selection),
                    atom2="(resi {} and name OG and {})".format(j, selection),
                )
            except:
                continue

            if asptoser < maxaadist and histoser < maxaadist:
                distspace["asphisdist"][accu].append(j)
    for i in distspace["asphisdist"]:
        if len(i) == 3:
            distspace["finallist"].append(i)
    print(distspace["finallist"])
    return
