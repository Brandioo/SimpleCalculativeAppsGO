score_tables = {
    ("R", "P"): (0, 1),
    ("R", "S"): (1, 0),
    ("P", "S"): (0, 1),
    ("P", "R"): (1, 0),
    ("S", "R"): (0, 1),
    ("S", "P"): (1, 0),
}

rounds = [["R", "P"], ["R", "S"], ["S", "P"]]

sokoli = 0
blerta = 0

for r in rounds:
    if r[0] == r[1]:
        continue
    s, b = score_tables[tuple(r)]
    sokoli += s
    blerta += b

print("Sokoli", sokoli, "-- Blerta", blerta)
