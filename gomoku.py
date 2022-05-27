import unittest
def Plansza():
    plansza = []
    for i in range(15):
        plansza.append([])
        for j in range(15):
            plansza[i].append('-')
    return plansza


def DrukujPlansze():
    print(' 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15')
    for i in range(len(plansza)):
        print(chr(i + ord('A')) + ' ', end='')
        for j in range(len(plansza)):
            print(plansza[i][j] + '  ', end='')
        print()


plansza = Plansza()


def Znak_Gracza():
    i = True
    while i == True:
        gracz1 = input("Wybierz symbol X lub O dla gracza 1: ")
        if gracz1 in ['x', 'X']:
            gracz1 = gracz1.upper()
            gracz2 = 'O'
            i = False
            print("Symbol pierwszego gracza: %s \nSymbol drugiego gracza: %s" % (gracz1, gracz2))
            return [gracz1, gracz2]
        elif gracz1 in ['o', 'O']:
            gracz2 = "X"
            i = False
            gracz1 = gracz1.upper()
            print("Symbol pierwszego gracza: %s \nSymbol drugiego gracza: %s" % (gracz1, gracz2))
            return [gracz1, gracz2]
        else:
            print("Błędy znak")


def Wiersz(pozycja, znak):
    start_x = max(0, pozycja[0] - 4)
    koniec_x = min(14, pozycja[0] + 4)
    count = 0
    for pozycja_x in range(start_x, koniec_x + 1):
        if plansza[pozycja_x][pozycja[1]] == znak:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False


def Kolumna(pozycja, znak):
    start_y = max(0, pozycja[1] - 4)
    koniec_y = min(14, pozycja[1] + 4)
    count = 0
    for pozycja_y in range(start_y, koniec_y + 1):
        if plansza[pozycja[0]][pozycja_y] == znak:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False


def Sprawdzenie1(pozycja, znak):
    if pozycja[0] >= pozycja[1]:
        start_punktu_y = max(0, pozycja[1] - 4)
        start_punktu_x = start_punktu_y + (pozycja[0] - pozycja[1])
        koniec_punktu_x = min(14, pozycja[0] + 4)
        koniec_punktu_y = koniec_punktu_x - (pozycja[0] - pozycja[1])
    else:
        start_punktu_x = max(0, pozycja[0] - 4)
        start_punktu_y = start_punktu_x - (pozycja[0] - pozycja[1])
        koniec_punktu_y = min(14, pozycja[1] + 4)
        koniec_punktu_x = koniec_punktu_y + (pozycja[0] - pozycja[1])

    count = 0
    for i, j in zip(range(start_punktu_x, koniec_punktu_x + 1), range(start_punktu_y, koniec_punktu_y + 1)):
        if plansza[i][j] == znak:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False


def Sprawdzenie2(pozycja, znak):
    s = sum(pozycja)
    if pozycja[0] + pozycja[1] <= 14:
        start_punktu_y = max(0, pozycja[1] - 4)
        start_punktu_x = s - start_punktu_y
        koniec_punktu_x = max(0, pozycja[0] - 4)
        koniec_punktu_y = s - koniec_punktu_x
    else:
        start_punktu_x = min(14, pozycja[0] + 4)
        start_punktu_y = s - start_punktu_x
        koniec_punktu_y = min(14, pozycja[1] + 4)
        koniec_punktu_x = s - koniec_punktu_y

    count = 0
    tmp_lst = list(range(koniec_punktu_x, start_punktu_x + 1))
    tmp_lst.reverse()
    for i, j in zip(tmp_lst, list(range(start_punktu_y, koniec_punktu_y + 1))):
        if plansza[i][j] == znak:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False


plansza = Plansza()


def Sprawdzenie_Koncowe(pozycja, znak):
    if Wiersz(pozycja, znak) or Kolumna(pozycja, znak) or Sprawdzenie1(pozycja, znak) or Sprawdzenie2(pozycja, znak):
        print(pozycja)
        return True
    else:
        return False


def main():
    print("Witamy w grze Gomoku!")
    znak = Znak_Gracza()
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
           'N': 13, 'O': 14}
    DrukujPlansze()
    i = True
    while i == True:
        choice = input('Ustal pozycję np. A3 lub A03 dla gracza ' + znak[0] + ": " + "(wyjście-e):")
        if choice == 'e':
            break
        elif not choice[0].isalpha() or not choice[1:].isdigit():
            print('Wprowadź poprawną pozycję!')
            continue
        else:
            choice_y = choice[0].title()
            choice_x = int(choice[1:]) - 1

        try:
            if 0 <= dic[choice_y] <= 14 and 0 <= choice_x <= 14:
                if plansza[dic[choice_y]][choice_x] != '-':
                    print('Ta pozycja jest już zajęta!')
                else:
                    if znak[0] == 'X':
                        plansza[dic[choice_y]][choice_x] = 'X'
                        if Sprawdzenie_Koncowe([dic[choice_y], choice_x], znak[0]) == True:
                            print('Gratulacje wygrywa gracz ze znakiem: %s!' % znak[0])
                            i = False
                        DrukujPlansze()
                        znak.reverse()
                    else:
                        plansza[dic[choice_y]][choice_x] = 'O'
                        if Sprawdzenie_Koncowe([dic[choice_y], choice_x], znak[0]) == True:
                            print('Gratulacje wygrywa gracz ze znakiem: %s!' % znak[0])
                            i = False
                        DrukujPlansze()
                        znak.reverse()
            else:
                print('Pozycja poza przedziałem!')
        except:
            print('Wprowadź poprawną pozycję!')


main()

class SprawdzenieKoncowe(unittest.TestCase):
    def test_Wiersz(self):
        self.assertEqual(False,Wiersz([1,10], ['O']))
    def test_Sprawdzenie1(self):
        self.assertEqual(False,Sprawdzenie1([2,4], ['O']))
    def test_Sprawdzenie2(self):
        self.assertEqual(False,Sprawdzenie2([6,9], ['X']))
    def test_Sprawdzenie_Koncowe(self):
        self.assertEqual(False,Sprawdzenie_Koncowe([4, 2],['X']))
    def test_Znak_Gracza(self):
        self.assertEqual(['X', 'O'],Znak_Gracza())
        
if __name__ == '__main__':
    unittest.main()



