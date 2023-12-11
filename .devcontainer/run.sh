xhost +local:root && docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -v /home/stask/Documents/Studia/7sem/Projekt_Niosr/niosr:/home/niosr \
    --net=host \
    --privileged \
    --name=niosr_project \
    -- niosr_project
    # ros2_lab:latest