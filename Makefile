install:
	pip install -r requirements.txt

run:
	python main.py

docker_build:
	docker build -t sorting_visualizer .

docker_run:
	docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd)/app:/app --rm sorting_visualizer