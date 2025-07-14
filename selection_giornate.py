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
            "fp_XYZ": 2270.25,
            "fp_PallaPazza": 2268.5,
            "fp_soros": 2239,
            "fp_PDG": 2202.5,
            "fp_Mainz": 2233.5,
            "fp_ignoranza": 2173.75,
            "fp_800a": 2138,
            "diseredati": 2062.25,
        },
        {
            "fp_XYZ": 2338.25,
            "fp_soros": 2305.5,
            "fp_PallaPazza": 2340.25,
            "fp_PDG": 2275.25,
            "fp_Mainz": 2302.25,
            "fp_ignoranza": 2303,
            "fp_800a": 2206.5,
            "diseredati": 2125.5,
        },
        {
            "fp_XYZ": 2407.5,
            "fp_soros": 2385.5,
            "fp_PallaPazza": 2405.25,
            "fp_PDG": 2344.75,
            "fp_Mainz": 2371.5,
            "fp_ignoranza": 2303,
            "fp_800a": 2253.75,
            "diseredati": 2183.5,
        },
    ]

    for variables in variables_by_giornata:
        variables["fp_totali"] = sum(variables.values())

    all_giornate = [
        calculate_giornate(variables) for variables in variables_by_giornata
    ]

    for giornate in all_giornate:
        print(giornate)
