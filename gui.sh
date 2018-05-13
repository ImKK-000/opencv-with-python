docker run --rm -it --net=host \
   -e DISPLAY \
   -v $PWD:/app \
   -w /app \
   jjanzic/docker-python3-opencv \
   bash

# pip install matplotlib