def gestion_col (mat, ligne, colonne):

    val = mat[ligne][colonne]

    if colonne == 0:
        return (True, val >= mat[ligne][colonne + 1])
    elif colonne == len (mat[0]) - 1:
        return (val >= mat[ligne][colonne - 1], True)
    else:
        return (val >= mat[ligne][colonne - 1], val >= mat[ligne][colonne + 1])


def pic_imp (mat):

    pics = []
    nb_lignes = len (mat)
    nb_colonnes = len (mat[0])
    for ligne in range (nb_lignes):
        for colonne in range (nb_colonnes):

            val = mat[ligne][colonne]

            if ligne == 0:
                haut = True
                bas = val >= mat[ligne + 1][colonne]
                gauche, droite = gestion_col (mat, ligne, colonne)

            elif ligne == nb_lignes - 1:
                haut = val >= mat[ligne - 1][colonne]
                bas = True
                gauche, droite = gestion_col (mat, ligne, colonne)

            else:
                haut = val >= mat[ligne - 1][colonne]
                bas = val >= mat[ligne + 1][colonne]
                gauche, droite = gestion_col (mat, ligne, colonne)

            if haut and bas and gauche and droite:
                pics.append ((val, ligne, colonne))

    return pics


def maxi_colonne_centrale (mat, colonne):

    maxi = mat[0][colonne]
    indice = 0
    for ligne in range (len (mat)):

        val = mat[ligne][colonne]
        if val > maxi:
            maxi = val
            indice = ligne

    return maxi, indice


def pic_rec (mat, colonne_debut, colonne_fin):

    nb_lignes = len (mat)
    nb_colonnes = colonne_fin - colonne_debut
    milieu = (colonne_debut + colonne_fin) // 2

    if nb_colonnes == 1:
        return (maxi_colonne_centrale (mat, colonne_debut)) + (colonne_debut,)

    elif nb_colonnes == 2:
        val, ligne = maxi_colonne_centrale (mat, colonne_debut)

        if mat[ligne][milieu - 1] <= val:
            return val, ligne, colonne_debut

        else:
            return (maxi_colonne_centrale (mat, colonne_fin)) + (colonne_fin,)
    
    else:
        val, ligne = maxi_colonne_centrale (mat, milieu)
        gauche = mat[ligne][milieu - 1] >= val

        if not gauche and val >= mat[ligne][milieu + 1]:
            return val, ligne, milieu

        elif gauche:
            return pic_rec (mat, colonne_debut, milieu)

        else:
            return pic_rec (mat, milieu + 1, colonne_fin)

    
print (pic_imp ([[9, 3, 5, 2, 4, 9, 8], [7, 2, 5, 1, 4, 0, 3], [9, 8, 9, 3, 2, 4, 8], [7, 6, 3, 1, 3, 2, 3], [9, 0, 6, 0, 4, 6, 4], [8, 9, 8, 0, 5, 3, 0], [2, 1, 2, 1, 1, 1, 1]]))
print (pic_rec ([[9, 3, 5, 2, 4, 9, 8], [7, 2, 5, 1, 4, 0, 3], [9, 8, 9, 3, 2, 4, 8], [7, 6, 3, 1, 3, 2, 3], [9, 0, 6, 0, 4, 6, 4], [8, 9, 8, 0, 5, 3, 0], [2, 1, 2, 1, 1, 1, 1]], 0, 6))
