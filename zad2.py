dane = [w.strip() for w in open('dane_6_1.txt').readlines()]
#print(dane)
def szyfr_cezara(s, k):
    #klucz_realny = k % (ord('Z') - ord('A') + 1)
    klucz_realny = k % 26
    wynik = ''
    for l in s:
        if ord(l) + klucz_realny > ord('Z'):
            wynik += chr(ord(l) + klucz_realny - 26)
        else:
            wynik += chr(ord(l) + klucz_realny)
    return wynik

#print(szyfr_cezara('KOT', 3))

plik_zapis = open('wynik2.txt', mode ='w+')

for s in dane:
    k = sum(map(ord, s))
    '''k = 0
    for l in s:
        k += ord(l)'''
    plik_zapis.write(szyfr_cezara(s, k) + '\n')
