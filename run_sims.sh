docker pull aitwatchman/simulation:latest
function sims()
{
  p=`pwd`'/shared/'
  docker run --rm -it \
    -v $p:/root/shared \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY \
    aitwatchman/simulation:latest
}

sims
exit
