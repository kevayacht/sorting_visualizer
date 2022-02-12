# sorting_visualizer

This project is a python sorting visualizer. 
The goal was to demonstrate OOP fundamentals in python alongside the application and visualization of various 
sorting algorithms. It's mainly done, because at the time of creation this seems to be a popular project for learning,
meaning the sorting visualization. The fundamentals were thrown in to help me continue writing good clean code.


`docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd)/app:/app --rm sorting_visualizer`

```
Install Xorg

Set $DISPLAY to: ":0:0" and "localhost:0:0"

Dig into tkinter file itsself (nothing useful there from what i can tell)

Turning laptop of and on, but only after applying all fixes at once...


docker run -u=$(id -u $USER):$(id -g $USER) \t
           -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
           -v $(pwd)/app:/app \
           --rm \
           -it \
           sorting_visualizer \
           /bin/bash
           
```