#include "include/csapp.h"

/* First address of handled region. */
#define ADDR_START ((void *)0x10000000)
/* Last address of handled region (not inclusive). */
#define ADDR_END ((void *)0x10010000)

static size_t pagesize;

/* Maps anonymouse page with `prot` access permissions at `addr` address. */
static void mmap_page(void *addr, int prot) {
  Mmap(addr, pagesize, prot, MAP_ANONYMOUS | MAP_PRIVATE | MAP_FIXED, -1, 0);
}

/* Changes protection bits to `prot` for page at `addr` address. */
static void mprotect_page(void *addr, int prot) {
  Mprotect(addr, pagesize, prot);
}

static void sigsegv_handler(int signum, siginfo_t *info, void *data) {
  ucontext_t *uc = data;
  intptr_t rip = uc->uc_mcontext.gregs[16];

  /* TODO: You need to get value of instruction pointer register from `uc`.
   * Print all useful data from `info` and quit in such a way that a shell
   * reports program has been terminated with SIGSEGV. */

  void* addr = info->si_addr;

  safe_printf("Fault at rip=%lx accessing %lx! ", (long unsigned int)rip, (long unsigned int)addr);

  if(ADDR_START > addr || addr >= ADDR_END){
    safe_printf("Address not mapped - terminating!\n");
    _exit(128 + SIGSEGV);
  }

  int errcode = info->si_code;
  void* page = addr - (intptr_t)addr % pagesize;

  if(errcode == SEGV_MAPERR) {
    safe_printf("Map missing page at %lx\n", (long unsigned int)page);
    mmap_page(page, PROT_READ);
  }

  if (errcode == SEGV_ACCERR){
    safe_printf("Make page at %lx writable.\n", (long unsigned int)page);
    mprotect_page(page, PROT_WRITE);
  }
}

int main(int argc, char **argv) {
  pagesize = sysconf(_SC_PAGESIZE);

  /* Register signal handler for SIGSEGV */
  struct sigaction action = {.sa_sigaction = sigsegv_handler,
                             .sa_flags = SA_SIGINFO};
  sigaction(SIGSEGV, &action, NULL);

  /* Initially all pages in the range are either not mapped or readonly! */
  for (void *addr = ADDR_START; addr < ADDR_END; addr += pagesize)
    if (random() % 2)
      mmap_page(addr, PROT_READ);

  /* Generate lots of writes to the region. */
  volatile long *array = ADDR_START;
  long nelems = (ADDR_END - ADDR_START) / sizeof(long);

  for (long i = 0; i < nelems * 2; i++) {
    long index = random() % nelems;
    array[index] = (long)&array[index];
  }

  /* Perform off by one access - triggering a real fault! */
  array[nelems] = 0xDEADC0DE;

  return EXIT_SUCCESS;
}
