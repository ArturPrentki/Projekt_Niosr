FROM ros:humble

WORKDIR /home/niosr
RUN ls /home/niosr

RUN apt-get update && apt-get -y upgrade && apt-get -y install ros-humble-desktop \
    git \
    vim \
    curl \
    ros-humble-turtlebot3* \
    gazebo\
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
COPY bashrc /home/niosr/.bashrc

# Set up entrypoint and default command
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]
