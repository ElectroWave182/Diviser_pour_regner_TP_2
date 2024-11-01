from random import randint


def meilleurMax0 (tab):

    ancien = tab[1]
    maxi = tab[0] + tab[1]
    for ele in tab:

        valeur = ele + ancien
        if valeur > maxi:
            maxi = valeur
        ancien = ele

    return maxi


def meilleurMax1 (tab):

    milieu = len (tab) // 2

    if len (tab) == 3:
        somme_1 = tab[0] + tab[1]
        somme_2 = tab[1] + tab[2]
        return max (somme_1, somme_2)

    elif len (tab) == 2:
        return tab[0] + tab[1]

    else:
        coupee = tab[milieu] + tab[milieu - 1]
        return max (meilleurMax1 (tab[: milieu]), meilleurMax1 (tab[milieu :]), coupee)


assert meilleurMax0 ([-1,9,-3,12,-5,4]) == 9
assert meilleurMax0 ([0, 0]) == 0

assert meilleurMax1 ([-1,9,-3,12,-5,4]) == 9
assert meilleurMax1 ([0, 0]) == 0

tableau = [[randint (0, 200) - 100 for _ in range (randint (2, 200))] for _ in range (100)]
for liste in tableau:
    assert meilleurMax0 (liste) == meilleurMax1 (liste)

# 4) c'est linéaire