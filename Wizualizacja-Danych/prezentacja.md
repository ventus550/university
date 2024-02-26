---
marp: true
theme: gaia
class: lead
style: |
  section {
    font-size: 24px;
  }
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

![bg left:40% 80%](https://i.pinimg.com/originals/23/50/09/235009158fa8f90d0f5f43c82bd5d5c3.png)

# **Flight Patterns**

<!-- Markdown Presentation Ecosystem

https://colab.research.google.com/drive/1PEDaFeRSVYp-NVyq9j5K53soEgpjAmly#scrollTo=gYdnZ2L197sQ -->

---

# **Plan prezentacji**
- Linie lotnicze
- Problem dużych danych
- Mapy cieplne
- Datashader
- Grupowanie krawędzi

---

# **Linie lotnicze**
![bg left:50%](http://www.aaronkoblin.com/work/flightpatterns/title.jpg)

Projekt ma na celu wizualizację trajektorii lotów na terenie Stanów Zjednoczonych i Kanady. Autorzy zwracają uwagę na to jak pomocna dla zrozumienia rozmiaru i rozpiętości linii lotniczych jest taka wizualizacja. Wszystkie trajektorie razem pokazują więcej niż suma każdych z osobna. Z danych i liczb wyłania się system.

---

## **Rezultat jest zaskakujący**
<!-- _theme: uncover -->

Efekt przewidywany         |  Efekt uzyskany
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/989466773277536268/1054020919439392788/image.png)  |  ![width:475px](https://cdn.discordapp.com/attachments/989466773277536268/1054020957368492032/image.png)

Widzimy od razu, że trajektorie układają się w powietrzne pasma. Ewidetnie niektóre trasy są z jakichś przyczyn bardziej uczęszczane.

___

## **Wykorzystanie koloru**
![bg left:50%](https://i.pinimg.com/originals/74/e4/f3/74e4f36c346e0bb76872925dd472e53d.jpg)

___

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://media.discordapp.net/attachments/989466773277536268/1054041525719404604/image.png)
*Kolor wskazuje wysokość, a czysta biel oznacza, że samolot znajduje się na ziemi*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://media.discordapp.net/attachments/989466773277536268/1054042099613442118/image.png)
*Kolor użyty w celu rozróżnienia modeli samolotów*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://media.discordapp.net/attachments/989466773277536268/1054042249333313566/image.png)
*Mapa pojedynczego modelu samolotu, pokazująca tylko loty Embraer ERJ 145*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://media.discordapp.net/attachments/989466773277536268/1054042283126816818/image.png)
*Mapa pojedynczego modelu samolotu, pokazująca tylko loty Boeing 737*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://cdn.discordapp.com/attachments/989466773277536268/1054042312252072017/image.png)
*Kolory niebieski i pomarańczowy to odpowiednio wzloty i lądowania*

---

## **Anomalie danych**
![bg left:50%](https://as1.ftcdn.net/v2/jpg/01/39/01/92/1000_F_139019211_Hj7GZnmrLtgYVNw4mLXK9sUrHtQpOT3V.jpg)
W danych często pojawiają się anomalie i nie jest to wyjątkiem również tutaj: 3000 samolotów, które raportowały swoje pozycje nie opuściwszy nigdy lotniska czy też lot przemierzający cały kraj w sześć minut. 

___

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://cdn.discordapp.com/attachments/989466773277536268/1054083039002632252/image.png)
*Poszarpane loty nad Atlantykiem*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://cdn.discordapp.com/attachments/989466773277536268/1054083649059966986/image.png)
*Zbliżenie na strefy zakazu lotów w południowo-zachodnich Stanach Zjednoczonych*

---

## **Kwestie techniczne**
![bg left:50%](https://upload.wikimedia.org/wikipedia/commons/c/c2/Processing_4.0b1_Icon.png)

[vid]: https://www.youtube.com/watch?v=ystkKXzt9Wk
Wizualizacja powstała przy użyciu języka programowania "Processing" dedykowanego wizualizacji danych, zbudowana na bazie zbioru z 2008 roku liczącego ponad 26 milionów punktów danych. Oprócz statycznego obrazu utworzono również stosowną [animację][vid].

___

# **Problem dużych danych**
![bg left:50%](https://wallpaperaccess.com/full/2005179.jpg)

---

# **Podejście klasyczne**
![bg](https://media.discordapp.net/attachments/989466773277536268/1053997509988589609/image.png)

[jup1]: https://colab.research.google.com/drive/1AcuBPEDMGbch_vHbUtsd3rs_AI9ki6wF?usp=sharing
[< jupyter notebook >][jup1]

---

## **Overplotting**
Gdy dwie kategorie **A** i **B** zostaną nałożone, wygląd wyniku może się bardzo różnić w zależności od tego, która z nich zostanie nakreślona jako pierwsza.

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053808105441464320/oTsciw9l0AAAAASUVORK5CYII.png)

Wykresy **C** i **D** wykazały ten sam rozkład punktów, ale dają bardzo różne wrażenie, która kategoria jest bardziej powszechna, co może prowadzić do błędnych decyzji na podstawie tych danych. Oczywiście obie są równie powszechne w tym przypadku, więc ani **C**, ani **D** nie odzwierciedlają dokładnie danych. Przyczyną tego problemu jest po prostu okluzja.

___

## **Przesycenie**
Problem można zredukować wprowadzając współczynnik przezroczystości alfa, przykładowo jeśli alfa wynosi 0.1, pełne nasycenie kolorów zostanie osiągnięte dopiero, gdy dziesięć punktów nałoży się na siebie.

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053817824583356466/uiH5z84jAAAAAElFTkSuQmCC.png)

Tutaj **C** i **D** zachowują się lepiej, ponieważ wyglądają bardzo podobnie, ale gdyby były naprawdę dokładnymi wykresami, byłyby identyczne, ponieważ rozkłady są identyczne. W tym przykładzie przesycone punkty znajdują się w pobliżu środka wykresu, ale jedynym sposobem sprawdzenia, czy tam są, byłoby nakreślenie obu wersji i porównanie lub zbadanie wartości pikseli, aby zobaczyć, czy któryś osiągnął pełne nasycenie. W miejscach, w których osiągnięto nasycenie, występują problemy podobne do overplottingu, ponieważ tylko dziesięć ostatnich naniesionych punktów wpłynie na ostateczny kolor.

___

## **Niedopróbkowanie**
W przypadku występowania tylko jednej kategorii przesycenie po prostu przesłania przestrzenne różnice w gęstości. Na przykład 10, 20 i 2000 nakładających się punktów pojedynczej kategorii będzie wyglądać tak samo wizualnie, dla alfa równego 0.1. Możemy tu zaobserwować, że rozmiar i alfa punktów wymagałaby dostosowywania do liczebności i zagęszczenia punktów.

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053819652901445642/MbEHSFyVNSrreOben5JAADCByDYBeI88A6AdyTbhGyg4Aw8XMPirpsnPuC2b2DknPmtlvOefozYAAwOcg2AXiPPAOgHck3Y6FABAAAAAAAoiGuoAAAAAAAAFERBBQAAAAAAoCAKKgAAAAAAAAVRUAEAAAAAACiIggoAAAAAAEBBFFQAAAAAAAAKoqACAAAAAABQ0P8DM1A1IShEBS4AAAAASUVORK5CYII.png)

Wraz ze wzrostem rozmiaru danych wykreślenie pełnego rozrzutu korzystając z metod klasycznych staje się coraz mniej praktyczne. W takiej sytuacji często próbuje się próbkować zbiór, ale jak pokazuje panel **A**, kształt niedopróbkowanego rozkładu może być bardzo trudny lub niemożliwy do rozpoznania, co prowadzi do błędnych wniosków na temat rozkładu.

___

## **Niedosycenie**
Wykresy **A**, **B** i **C** są wykresami rozrzutu dla tych samych danych, które są sumą 5 rozkładów normalnych w różnych miejscach i o różnych odchyleniach standardowych.

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053818593592233994/cPYyMsHAAAAAElFTkSuQmCC.png)

Każdy z pięciu rozkładów ma taką samą liczbę punktów danych, ale drugi co do wielkości wygląda na więcej niż pozostałe, a najwęższy prawdopodobnie zostanie całkowicie pominięty, co jest zatem wyraźnym przykładem przesycenia. Jeśli jednak spróbujemy zwalczyć przesycenie za pomocą przezroczystości w **C**, mamy teraz wyraźny problem z niedosyceniem – „bardzo duży rozrzut” normalny jest teraz zasadniczo niewidoczny. Ponownie, w tej kategorii jest tyle samo punktów danych, ale nigdy byśmy nawet nie wiedzieli, że tam są, patrząc tylko na **C**.

---

# **Mapy cieplne**
![bg left:50%](https://img.freepik.com/free-vector/gradient-heat-map-background_23-2149528514.jpg?w=2000&t=st=1671366221~exp=1671366821~hmac=867048b0a1e426b524f2517667f0b4453fd51bf7d5f2884d62ff51b2eb193ff4)

Aby uniknąć niedopróbkowania dużych zestawów danych, badacze często używają dwuwymiarowych histogramów wizualizowanych jako mapy cieplne, zamiast wykresów rozrzutu przedstawiających poszczególne punkty. Mapa cieplna ma siatkę o stałym rozmiarze, niezależnie od rozmiaru zestawu danych, dzięki czemu można wykorzystać wszystkie dane. Mapy cieplne skutecznie aproksymują funkcję gęstości prawdopodobieństwa w określonej przestrzeni, przy czym grubsze mapy cieplne uśredniają szum lub nieistotne zmiany w celu ujawnienia podstawowego rozkładu, a dokładniejsze mapy cieplne mogą przedstawiać więcej szczegółów w rozkładzie.

---

Przyjrzyjmy się niektórym mapom cieplnym z różnym doborem wymiarów siatki.

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053875845518852106/Zoxi9O2wdToAAAAASUVORK5CYII.png)

Można szybko zauważyć, że **B** stanowi najlepsze przybliżenie rozkładu, podczas gdy **C** przypomina jego próbkowanie. W związku z tym wybór odpowiedniego rozmiaru siatki dla mapy cieplnej wymaga pewnej wiedzy i znajomości celów wizualizacji, a dla porównania zawsze warto przyjrzeć się ustawieniom wielu siatek.

---

## **Problemy rozwiązywane przez mapy cieplne**
  - overplotting — wiele punktów danych sumuje się arytmetycznie w komórce siatki, bez zasłaniania się nawzajem
  - przesycenie — zaobserwowane minimalne i maksymalne zliczenia mogą być automatycznie mapowane na dwa końce widocznego zakresu kolorów
  - niedopróbkowanie — ponieważ wynikowy rozmiar wykresu jest niezależny od liczby punktów danych, co pozwala na wykorzystanie nieograniczonej ilości przychodzących danych

---

## **Każde rozwiązanie ma swój problem**
![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053864579660271616/VOschmvkAAAAASUVORK5CYII.png)

Rzeczywista struktura nadal nie jest widoczna. W przypadku **A** problemem jest ewidentnie zbyt zgrubne kategoryzowanie, w **B** dwa najmniejsze rozkłady ukazują się identycznie, a w **C** nadal wygląda bardziej jak wykres rozkładu o największy rozrzucie.

---

Problem jest teraz bardziej subtelny: różnice w gęstości punktów danych nie są widoczne między pięcioma rozkładami, ponieważ prawie wszystkie piksele są mapowane albo na dolny koniec widzialnego zakresu (jasnoszary), albo na górny koniec (czarny).  Spróbujmy więc przekształcić dane z ich domyślnej reprezentacji liniowej (wartości liczb całkowitych) w coś, co zachowuje względne różnice w wartościach liczb, ale odwzorowuje je na wizualnie różne kolory. Transformacja logarytmiczna jest jednym z powszechnych wyborów:

![width: 400px](https://media.discordapp.net/attachments/989466773277536268/1053885953946681414/SDJKiUwyKAAAAAElFTkSuQmCC.png)

Nie jest to jednak wystarczające. Wybór transformacji logarytmicznej był dość arbitralny i działa dobrze głównie dlatego, że podczas konstruowania przykładu zastosowaliśmy w przybliżeniu geometryczną progresję rozrzutów. Czy w przypadku dużych zbiorów danych o naprawdę nieznanej strukturze możemy zastosować bardziej pryncypialne podejście do mapowania wartości zbioru danych na widoczny zakres?

---

*Tak, jeśli pomyślimy o problemie wizualizacji w inny sposób. Podstawowa trudność w wykreśleniu tego zestawu danych (jak w przypadku bardzo wielu rzeczywistych zestawów danych) polega na tym, że wartości w każdym przedziale są liczbowo bardzo różne (od 10 000 w przedziale dla „bardzo wąskiego rozrzutu” Gaussa do 1 (dla pojedynczego punktów danych z „bardzo dużego rozrzutu” Gaussa)). Biorąc pod uwagę 256 poziomów szarości dostępnych na normalnym monitorze (i podobnie ograniczoną ludzką zdolność wykrywania różnic w wartościach szarości), numeryczne mapowanie wartości danych na widzialny zakres nie będzie działać dobrze. Ale biorąc pod uwagę, że wycofujemy się już z bezpośredniego mapowania numerycznego w powyższych podejściach do korygowania niedosycenia i wykonywania transformacji logarytmicznych, co by było, gdybyśmy całkowicie zrezygnowali z podejścia do mapowania numerycznego, używając liczb tylko do częściowego uporządkowania wartości danych? Takie podejście byłoby wykresem kolejności rang, zachowującym porządek, a nie wielkości. W przypadku 100 wartości szarości można myśleć o tym jako o wykresie opartym na percentylach, gdzie najniższy 1% wartości danych jest mapowany na pierwszą widoczną wartość szarości, następny 1% jest mapowany na następną widoczną wartość szarości itd. górny 1% wartości danych jest mapowany na szarą wartość 255 (w tym przypadku czarny). Rzeczywiste wartości danych byłyby ignorowane na takich wykresach, ale ich względne wielkości nadal określałyby, w jaki sposób odwzorowują kolory na ekranie, zachowując raczej strukturę rozkładu niż wartości liczbowe.*
⚠⚠⚠

---

![width: 400px](https://cdn.discordapp.com/attachments/989466773277536268/1053999937555279933/Tneh4gAAAABJRU5ErkJggg.png)
*Możemy przybliżyć takie kodowanie rangowe lub percentylowe za pomocą funkcji wyrównywania histogramu z pakietu do przetwarzania obrazu, który zapewnia, że każdy poziom szarości jest używany dla mniej więcej tej samej liczby pikseli na wykresie.*

---

## **Dobór zakresu widzialnego**
Mapa cieplna wymaga mapy kolorów, zanim będzie można ją zwizualizować. Niestety, większość map kolorów powszechnie używanych w oprogramowaniu graficznym jest wysoce niejednolita.

![](https://cdn.discordapp.com/attachments/989466773277536268/1054005164417232967/image.png) ![](https://cdn.discordapp.com/attachments/989466773277536268/1054005514234769440/image.png)

![](https://media.discordapp.net/attachments/989466773277536268/1054004140449222736/oxYqRVEURVGUNtEYKkVRFEVRlDZRQaUoiqIoitImKqgURVEURVHaRAWVoiiKoihKm6igUhRFURRFaRMVVIqiKIqiKG2igkpRFEVRFKVNVFApiqIoiqK0yf8PKDlOSxawtw8AAAAASUVORK5CYII.png)

*Zakres wartości mapy **B** będzie wyświetlany w odcieniach czerwieni, które są percepcyjnie nierozróżnialne.*

---

## **Podsumowanie**

![](https://media.discordapp.net/attachments/989466773277536268/1054006328504352868/xjEmWoWYLDEAAAAAElFTkSuQmCC.png)

Czy nie da się lepiej?

---

# **Datashader**

![bg 64% left:50%](https://media.discordapp.net/attachments/989466773277536268/1054018234254364793/image.png)

Czyli mocno zoptymalizowana bliblioteka do Pythona automatyzująca proces wizualizacji dużych danych.

https://datashader.org/index.html

---

  Małe dane                |  Duże dane
:-------------------------:|:-------------------------:
![width:475px](https://media.discordapp.net/attachments/989466773277536268/1054013777240141904/GnQi15Jb8LgAAAABJRU5ErkJggg.png)  |  ![width:475px](https://cdn.discordapp.com/attachments/989466773277536268/1054013817312514108/jsAvwfMLVCxyFdOOfg4OeWMRJIFIZERF7QubSfRWA3cemcswBP4DfTERfccBTizgRxIw5IiIiYmaIGXNERETEzBADc0RERMTMEANzRERExMwQA3NERETEzBADc0RERMTMEANzRERExMwQA3NERETEzBADc0RERMTMEANzRERExMwQA3NERETEzBADc0RERMTM8P8DcAFiX2wV0QYAAAAASUVORK5CYII.png)

---

## **Co można stworzyć w narzędziu Datashader?**

![bg left:50%](https://media.discordapp.net/attachments/989466773277536268/1054014150528995358/sym_attractors.png)

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:500px](https://media.discordapp.net/attachments/989466773277536268/1054014537927499786/8B8v8Dq7tUF3hEGooAAAAASUVORK5CYII.png)
*New York taxi trips*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:500px](https://www.architecture-performance.fr/wp-content/uploads/2018/09/raster_datashader.jpg)
*Nighttime lights*

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:500px](https://1.bp.blogspot.com/-KfcHdQ984Ms/V-jF0ZJYhpI/AAAAAAAABNo/PxiitMKcyqo0BRaN8t-15z5vjOejbWARQCLcB/s1600/datashader_global_seismicity_3_0.png)
*Seismic activity*

---

## **Jak to działa?**
![width:800px](https://datashader.org/assets/images/pipeline2.png)

[jup4]: https://colab.research.google.com/drive/1z49FiLHbm7gkeQyh51AqN7BIGDFQNKRu?usp=sharing
[< jupyter notebook >][jup4]

---

## **A jak jest z szybkością?**
[int]: https://nyc-taxi.pyviz.demo.anaconda.com/dashboard
[more]: https://datashader.org/user_guide/Performance.html
Najpierw musimy porozmawiać o oryginalnym formacie danych. Datashader jest tak szybki, że wczytywanie danych jest zwykle najwolniejszym krokiem. Obliczenia agregacji Datashadera są pisane w Pythonie, a następnie kompilowane just-in-time w niesamowicie szybki kod maszynowy przy użyciu Numby. Datashader może również zrównoleglić swój potok. onieważ Datashader jest tak szybki, możemy interaktywnie wizualizować duże zbiory danych, dynamicznie przerysowując je za każdym razem, gdy powiększamy lub przesuwamy. Oto przykład, w którym można interaktywnie przeglądać dane z [NYC Taxi][int] na pulpicie nawigacyjnym Panelu. [(więcej o wydajności)][more]

---

## **Linie lotnicze w Datashader**
![bg left:50%](https://media.discordapp.net/attachments/989466773277536268/1054074535479091250/wEr3pzywQrZagAAAABJRU5ErkJggg.png)

[jup2]: https://examples.pyviz.org/opensky/opensky.html
[< source code >][jup2]

---

# **Grupowanie krawędzi**
![bg left:50%](https://www.data-to-viz.com/graph/IMG/bundle_map.png)

[sp]: https://courses.isds.tugraz.at/ivis/surveys/ss2017/ivis-ss2017-g4-survey-edge-bundling.pdf
[< algorytmy >][sp]

---

## **Wizualizacja sąsiedztwa**
![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://www.data-to-viz.com/graph/edge_bundling_files/figure-html/unnamed-chunk-2-1.png)

---

## **Odśmiecanie wizualizacji**
![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:800px](https://seeingcomplexity.files.wordpress.com/2011/02/bundle2.png)

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:600px](https://pbs.twimg.com/media/EI9eNqsU0AEBiFr.jpg:large)

[int2]: https://observablehq.com/@d3/hierarchical-edge-bundling
[< interactive tool >][int2]

---

![drop-shadow:0,5px,10px,rgba(0,0,0,.4) width:600px](https://media.discordapp.net/attachments/336118091844943873/1054144035192836297/image.png?width=1536&height=1561)

[int3]: https://anaconda.org/philippjfr/packet_capture_graph_hv/notebook
[< interactive tool >][int3]

---

## **Grupowanie linii lotniczych**
![bg left:50%](https://media.discordapp.net/attachments/989466773277536268/1054076350161490040/ARA2CjxDm3w6AAAAAElFTkSuQmCC.png)

[jup3]: https://colab.research.google.com/drive/1PEDaFeRSVYp-NVyq9j5K53soEgpjAmly?usp=sharing
[< jupyter notebook >][jup3]

