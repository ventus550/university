#include "csapp.h"

#define DIRBUFSZ 256

static void print_mode(mode_t m) {
  char t;

  if (S_ISDIR(m))
    t = 'd';
  else if (S_ISCHR(m))
    t = 'c';
  else if (S_ISBLK(m))
    t = 'b';
  else if (S_ISREG(m))
    t = '-';
  else if (S_ISFIFO(m))
    t = 'f';
  else if (S_ISLNK(m))
    t = 'l';
  else if (S_ISSOCK(m))
    t = 's';
  else
    t = '?';

  char ur = (m & S_IRUSR) ? 'r' : '-'; // Read by owner
  char uw = (m & S_IWUSR) ? 'w' : '-'; // Write by owner
  char ux = (m & S_IXUSR) ? 'x' : '-'; // Execute by owner
  char gr = (m & S_IRGRP) ? 'r' : '-'; // Read by group
  char gw = (m & S_IWGRP) ? 'w' : '-'; // Write by group
  char gx = (m & S_IXGRP) ? 'x' : '-'; // Execute by group
  char or = (m & S_IROTH) ? 'r' : '-'; // Read by others
  char ow = (m & S_IWOTH) ? 'w' : '-'; // Write by others
  char ox = (m & S_IXOTH) ? 'x' : '-'; // Execute by others

  /* TODO: Fix code to report set-uid/set-gid/sticky bit as 'ls' does. */
  gx = (m & S_ISUID) ? ((gx == 'x' ? 's' : 'S')) : gx;
  ux = (m & S_ISGID) ? ((ux == 'x' ? 's' : 'S')) : ux;
  ox = (m & S_ISVTX) ? ((ox == 'x' ? 't' : 'T')) : ox;

  printf("%c%c%c%c%c%c%c%c%c%c", t, ur, uw, ux, gr, gw, gx, or, ow, ox);
}

static void print_uid(uid_t uid) {
  struct passwd *pw = getpwuid(uid);
  if (pw)
    printf(" %10s", pw->pw_name);
  else
    printf(" %10d", uid);
}

static void print_gid(gid_t gid) {
  struct group *gr = getgrgid(gid);
  if (gr)
    printf(" %10s", gr->gr_name);
  else
    printf(" %10d", gid);
}

static void file_info(int dirfd, const char *name) {
  struct stat sb[1];

  /* TODO: Read file metadata. */
  Fstatat(dirfd, name, sb, AT_SYMLINK_NOFOLLOW);

  print_mode(sb->st_mode);
  printf("%4ld", sb->st_nlink);
  print_uid(sb->st_uid);
  print_gid(sb->st_gid);

  /* TODO: For devices: print major/minor pair; for other files: size. */
  if (S_ISCHR(sb->st_mode) || S_ISBLK(sb->st_mode))
    printf(" %5u,%5u", major(sb->st_rdev), minor(sb->st_rdev));
  else
    printf(" %11ld", sb->st_size);

  char *now = ctime(&sb->st_mtime);
  now[strlen(now) - 1] = '\0';
  printf("%26s", now);

  printf("  %s", name);

  if (S_ISLNK(sb->st_mode)) {
  /* TODO: Read where symlink points to and print '-> destination' string. */
    char symlink[PATH_MAX];
    Readlinkat(dirfd, name, symlink, PATH_MAX);
    printf(" -> %s", symlink);
  }

  putchar('\n');
}

int main(int argc, char *argv[]) {
  if (!argv[1])
    argv[1] = ".";

  int dirfd = Open(argv[1], O_RDONLY | O_DIRECTORY, 0);
  char buf[DIRBUFSZ];
  int n;

  while ((n = Getdents(dirfd, (void *)buf, DIRBUFSZ))) {
    struct linux_dirent *d;
    
    /* TODO: Iterate over directory entries and call file_info on them. */
    for (int i = 0; i < n; i += d->d_reclen) {
      d = (struct linux_dirent *)(buf + i);
      file_info(dirfd, d->d_name);
    }
  }

  Close(dirfd);
  return EXIT_SUCCESS;
}
