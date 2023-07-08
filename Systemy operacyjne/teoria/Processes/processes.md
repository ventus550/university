# Processes

## Fork
Tworzy nowy proces poprzez pączkowanie, tj. kopiując inny proces.

However, copying memory is expensive, so all modern Linux systems cheat.
They giv e the child its own page tables, but have them point to the parent’s pages,
only marked read only. Whenever either process (the child or the parent) tries to
write on a page, it gets a protection fault. The kernel sees this and then allocates a
new copy of the page to the faulting process and marks it read/write. In this way,
only pages that are actually written have to be copied. This mechanism is called
copy on write. It has the additional benefit of not requiring two copies of the program in memory, thus saving RAM.

