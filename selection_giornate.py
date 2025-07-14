from collections import OrderedDict

MIN_GIORNATA = 6
MAX_GIORNATA = 34

def calculate_giornate(variables: dict[str, float]) -> list[float]:
    giornate = OrderedDict()
    for value in variables.values():
        value = int(value)
        giornata = MIN_GIORNATA + value % (MAX_GIORNATA - MIN_GIORNATA + 1)
        added = False
        if giornata not in giornate:
            giornate[giornata] = None
            added = True
        else:
            while giornata in giornate and giornata < MAX_GIORNATA:
                giornata += 1
                if giornata not in giornate:
                    giornate[giornata] = None
                    added = True
                    break
            if added is False:
                while giornata in giornate and giornata > MIN_GIORNATA:
                    giornata -= 1
                    if giornata not in giornate:
                        giornate[giornata] = None
                        added = True
                        break
        if added is False:
            raise ValueError("Mi cunfunnii")

    # extra check:
    for giornata in giornate:
        if giornata < MIN_GIORNATA or giornata > MAX_GIORNATA:
            raise ValueError(f"Giornata cannot be {giornata}")

    return [giornata for giornata in giornate]


if __name__ == "__main__":

    variables_by_giornata = [
        {
            "fp_XYZ": 2407.5,
            "fp_Soros": 2385.5,
            "fp_PallaPazza": 2405.25,
            "fp_PDG": 2344.75,
            "fp_Mainz": 2371.5,
            "fp_Ignoranza": 2303,
            "fp_800a": 2253.75,
            "fp_Diseredati": 2183.5,
        },
    ]

    for index, variables in enumerate(variables_by_giornata):
        variables_by_giornata[index] = {team: variables[team] for team in sorted(variables)}

    for variables in variables_by_giornata:
        variables["fp_totali"] = sum(variables.values())

    all_giornate = [
        calculate_giornate(variables) for variables in variables_by_giornata
    ]

    for giornate in all_giornate:
        print(giornate)
