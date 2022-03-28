from pathlib import Path
import vim
import sys

cohledam = str(sys.argv[1])
predret: str = "-I/"
nahrada: str = ""
cesta = Path(vim.eval("expand('%:p:h')"))
pocet = len(cesta.parents)
what_find: str = ".ccls"


def hledam(my_file: str, where: Path):
    # Otevřeme soubor
    with open(file=where, encoding="utf8") as ff:
        # a budem ho procházet řádek po řádku
        for i in ff:
            # pokud řádek začíná s 'predret' tak obsahuje cestu
            if i.startswith(predret):
                # vyseparujem cestu z řetězce a uříznem znak konce řádku
                ce = Path(i.replace(predret[:2], nahrada)[:-1])
                # k ní přidáme název hledaného souboru
                # a odzkoušíme či soubor existuje
                if ce.joinpath(my_file).is_file():
                    # pokud existuje vrátíme jeho kompletní cestu
                    return str(ce.joinpath(my_file))
    return "./"+my_file


def vysledek():
    mezi = 0
    while mezi < pocet-3:
        if (cesta.parents[mezi].joinpath(what_find).is_file()):
            return cesta.parents[mezi].joinpath(what_find)
        mezi += 1


vim.command("let blabla='" + hledam(cohledam, vysledek()) + "'")
