FROM ros:humble

RUN apt-get update && apt-get -y upgrade && apt-get -y install ros-humble-desktop