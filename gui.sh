xhost +
sudo docker run --rm -ti --net=host --ipc=host \
   -e DISPLAY=$DISPLAY \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   -v $PWD:/app \
   jjanzic/docker-python3-opencv \
   bash