import vim

# získáme typ souboru podle přípony
act_file = str(vim.eval("expand('%:e')"))
# k typu souboru přiřadíme komentovací sekvenci
fil_com = {'py': '# ', 'c': '// ', 'cpp': '// ', 'vim': '" ', 'lua': '--', 'ino': '// ', 'dart': '// '}
# na základě typu souboru vybereme aktuální komentstring
try:
    comstring = fil_com[act_file]
except KeyError:
    # pokud není klíč (neznámý soubor) přiřaď do hodnoty prázdný řetězec
    comstring = ""

# vytvoříme instanci
okno = vim.current


def add_spaces(num):
    # fce vrátí řetězec mezer o délce 'num'
    a = ""
    for i in range(num):
        a += " "
    return a


for i in okno.range:
    # Hned na začátku otestujem jestli je řádek prázdný
    if not i:
        # pokud je prázdný ukončíme aktuální cykl
        continue
    # řádek není prázdný jedem dál
    # oříznem všechny mezery na začátku řetězce a zbytek si uložíme
    after = i.lstrip(" ")
    # získáme odsazení řádku rozdílem délky originálu a zbytku
    pre = len(i) - len(after)
    # prestr bude obsahovat řetězec mezer nebo nic podle odsazení řádku
    prestr = add_spaces(pre)
    # načtem pozici kurzoru
    row, col = okno.window.cursor
    if i.lstrip(" ").startswith(comstring):
        # odříznem commentstring
        after = after.lstrip(comstring)
        # spojíme indent se zbytkem řádku a uložíme to do aktuálního řádku
        okno.line = prestr + after
        # spočítáme místo kurzoru
        col = col - len(comstring)
        # ternálním operátorem ošetříme nepřípustnou hodnotu <1
        col = (1, col)[col > 1]
    else:
        # spojíme indent s commentstringem a zbytkem řádku a uložíme to do
        # aktuálního řádku
        okno.line = prestr + comstring + after
        # spočítáme místo kurzoru
        col = col + len(comstring)
    # posuneneme kurzor na správné místo
    okno.window.cursor = (row, col)
