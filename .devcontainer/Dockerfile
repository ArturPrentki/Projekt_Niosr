FROM ros:humble

WORKDIR /home/niosr
RUN ls /home/niosr

RUN apt-get update && apt-get -y upgrade && apt-get -y install ros-humble-desktop \
    git \
    vim \
    curl 

COPY bashrc-git-prompt /tmp/
RUN curl -L https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh >> /etc/skel/.bashrc \
    && cat /tmp/bashrc-git-prompt >> /etc/skel/.bashrc \
    && rm -rf /tmp/bashrc-git-prompt \
    && echo "source /opt/ros/humble/setup.bash" >> /etc/skel/.bashrc

