FROM ros:humble

WORKDIR /root/niosr
RUN ls /root/niosr

RUN apt-get update && apt-get -y upgrade && apt-get -y install ros-humble-desktop \
    git \
    vim \
