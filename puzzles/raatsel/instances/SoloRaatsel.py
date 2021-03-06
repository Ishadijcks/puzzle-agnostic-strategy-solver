from puzzles.raatsel.Raatsel2x2 import Raatsel2x2


def get_realistic_2x2_raatsel():
    words = ["Solo", "Aria", "Solitaire", "Patience", "Pesten", "Pennywafel", "Piano", "Rietveld", "Dam", "Duiker",
             "Berger", "Cantor", "Koster", "Pastoor", "Enrique", "Reiziger", "Romer", "Noten", "Kwartet", "Jokeren",
             "Lotus", "Koraal", "Moslim", "Ensemble", "Opera", "Hotel", "Mariakapel", "Boothuis", "Pagode", "Kerk"]
    matrix = [
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # W0
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],  # W1
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # W2
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # W3
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # W4
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # W5
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # W6
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # W7
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # W8
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # W9
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # W10
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # W11
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # W12
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # W13
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # W14
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],  # W15
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],  # W16
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],  # W17
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # W18
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # W19
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # W20
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],  # W21
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # W22
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # W23
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # W24
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # W25
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  # W26
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # W27
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # W28
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # W29
    ]
    categories = ["Muziek", "Spel", "Meisjesnaam", "In het water", "Religieus", "Zelfde begin- en eindletter",
                  "Bouwwerk"]

    edges = ["Alleen", "P", "Architect", "6 letters", "Voetbalcoach", "Han"]
    return Raatsel2x2(
        words,
        categories,
        edges,
        matrix
    )