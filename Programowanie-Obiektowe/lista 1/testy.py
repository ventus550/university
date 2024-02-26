import figury
import ulamki
import tablica


#---------Figury----------------
f = figury.Figura()
f = figury.nowa_figura('kwadrat', -5, 5, 10)

print('pole:' , figury.pole(f))

figury.przesun(f, 100, 100)

print('xy:' ,f.x, f.y)

#---------Ulamki----------------
u1 = ulamki.Ulamek()
u2 = ulamki.Ulamek()
u = ulamki.Ulamek()

u1 = ulamki.nowy_ulamek(3, -9)
u2 = ulamki.nowy_ulamek(7, 3)


u = ulamki.dodaj(u1, u2)

print('licznik/mianownik:' ,u.licznik, u.mianownik)



#---------Tablica----------------

t = tablica.Tablica()
tablica.dodaj(t, 0, 'kot')

print(tablica.indeks(t, 0), tablica.indeks(t, -1))