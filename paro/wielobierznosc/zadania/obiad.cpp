#include <future>
#include <iostream>
#include "obiad.hpp"

Herbata                zrob_herbate(Woda, TorebkaHerbaty);
PokrojonySurowyKurczak pokroj_kurczaka(SurowyKurczak);
GotowyKurczak          usmaz_kurczaka(PokrojonySurowyKurczak);
UgotowaneZiemniaki     ugotuj_ziemniaki(Woda, SuroweZiemniaki);
Obiad                  zrob_obiad(UgotowaneZiemniaki, GotowyKurczak, Herbata);


Obiad ugotuj()
{
  // To dostajecie
  Woda            woda;
  SuroweZiemniaki suroweZiemniaki;
  SurowyKurczak   surowyKurczak;
  TorebkaHerbaty  torebkaHerbaty;

  // TODO: tutajo
  auto f1 = std::async(std::launch::async, zrob_herbate, woda, torebkaHerbaty);
  auto f2 = std::async(std::launch::async, pokroj_kurczaka, surowyKurczak);
  auto f3 = std::async(std::launch::async, ugotuj_ziemniaki, woda, suroweZiemniaki);
  auto f4 = std::async(std::launch::async, usmaz_kurczaka, f2.get());
  return zrob_obiad(f3.get(), f4.get(), f1.get());
}



int main()
{
  auto  start  = Clock::now();
  Obiad obiad1 = synchroniczneGotowanie();
  auto  stop  = Clock::now();
  std::cout << "Synchronicznie: "
            << std::chrono::duration_cast<std::chrono::milliseconds>(stop - start).count()
            << "[ms]" << std::endl;

  start        = Clock::now();
  Obiad obiad2 = ugotuj();
  stop         = Clock::now();
  std::cout << "Twoja implementacja: "
            << std::chrono::duration_cast<std::chrono::milliseconds>(stop - start).count()
            << "[ms]" << std::endl;
}
