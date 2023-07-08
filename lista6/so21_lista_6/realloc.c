#include "csapp.h"

static int getid(uid_t *uid_p, gid_t *gid_p, gid_t **gids_p) {
  gid_t *gids = NULL;
  int ngid = 2;
  int groups;

  /* TODO: Something is missing here! */
  *uid_p = getuid();
  *gid_p = getgid();

  while ((groups = getgroups(ngid + 1, gids)) < 0) {
    ngid++;
    gids = realloc(gids, ngid * sizeof(gid_t));
  }
  
  *gids_p = gids;
  return groups;
}