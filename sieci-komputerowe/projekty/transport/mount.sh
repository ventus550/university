rm -rf /tmp/virbian{1..4}
mkdir /tmp/virbian{1..4}

for x in {1..4}; do
  sshfs -p 302$x user@localhost:/home/user /tmp/virbian$x
done
