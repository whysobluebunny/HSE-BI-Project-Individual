
def process():
    names = {"sequence", "h2a_1", "h2b_1", "h3_1", "h4_1"}
    namesfiles = {"c.elegans", "ciliate", "drosophila", "e.coli",
                  "human", "methanocaldococcus", "mouse",
                  "thermococcus", "tuberculosis", "yeast", "zebrafish"}
    path = "/Users/whysobluebunny/bio/abondarenko"
    for name in names:
        print("{name} ".format(name=name), end="")
        for filename in namesfiles:
            with open("{path}/{name}/{file}.blast".format(path=path, name=name, file=filename)) as file:
                for i, line in enumerate(file):
                    if i == 5:
                        splitted = line.split("\t")
                        print("{file}: {value} ".format(file=filename, value=splitted[-2]), end='')
        print()


if __name__ == '__main__':
    process()

