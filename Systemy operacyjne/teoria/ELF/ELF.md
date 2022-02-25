# ELF - Executable and Linkable File
ELF są plikami relokowalnymi i obiektowymi zatem obsługują
np. `objdump` i mają rozszerzenie ".o".

- `pliki relokowalne` -- pliki generowane przez kompilator,
przeznaczone do późniejszego przetworzenia przez konsolidator.
- `konsolidator` -- (ang. linker) łączy pliki obiektowe w plik wykonywalny



![](file:///home/ventus/OneDrive/Documents/uwr/SO/inne/teoria/ELF/ELF.png)

The format of an executable object ﬁle is similar to that of a relocatable object
ﬁle. The ELF header describes the overall format of the ﬁle. It also includes the
program’s entry point, which is the address of the ﬁrst instruction to execute when
the program runs. The .text, .rodata, and .data sections are similar to those in
a relocatable object ﬁle, except that these sections have been relocated to their
eventual run-time memory addresses. The .init section deﬁnes a small function,
called _init, that will be called by the program’s initialization code. Since the
executable is fully linked (relocated), it needs no .rel sections.
ELF executables are designed to be easy to load into memory, with contigu-
ous chunks of the executable ﬁle mapped to contiguous memory segments. This
mapping is described by the segment header table. 

```c
(Figure 7.12)

1 LOAD off 0x00000000 vaddr 0x08048000 paddr 0x08048000 align 2**12
2 filesz 0x00000448 memsz 0x00000448 flags r-x

3 LOAD off 0x00000448 vaddr 0x08049448 paddr 0x08049448 align 2**12
4 filesz 0x000000e8 memsz 0x00000104 flags rw-
```
Figure 7.12 shows the segment
header table for our example executable p, as displayed by objdump.
From the segment header table, we see that two memory segments will be
initialized with the contents of the executable object ﬁle. Lines 1 and 2 tell us
that the ﬁrst segment (the code segment) is aligned to a 4 KB (2 12 ) boundary,
has read/execute permissions, starts at memory address 0x08048000, has a total
memory size of 0x448 bytes, and is initialized with the ﬁrst 0x448 bytes of the
executable object ﬁle, which includes the ELF header, the segment header table,
and the .init, .text, and .rodata sections.
Lines 3 and 4 tell us that the second segment (the data segment) is aligned to a
4 KB boundary, has read/write permissions, starts at memory address 0x08049448,
has a total memory size of 0x104 bytes, and is initialized with the 0xe8 bytes
starting at ﬁle offset 0x448, which in this case is the beginning of the .data section.
The remaining bytes in the segment correspond to .bss data that will be initialized
to zero at run time.

## Sekcje i segmenty
- Sekcje są wykorzystywane w procesie linkowania i relokacji
- Segmenty przechowują dane potrzebne do wykonania prgramu


## Narzędzia
- `ar` -- zarządzanie plikami archiwalnymi
- `objdump` -- analiza plików obiektowych
- `readelf` -- analiza plików ELF
