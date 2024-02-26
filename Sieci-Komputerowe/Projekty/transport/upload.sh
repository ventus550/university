for x in {1..4}; do

  if [ -d /tmp/virbian$x/router ]
  then
    rm -rf /tmp/virbian$x/router/*
  else
    mkdir /tmp/virbian$x/router
  fi

  cp -r ./* /tmp/virbian$x/router
done
