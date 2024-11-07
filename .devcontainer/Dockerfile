FROM ubuntu:22.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    curl \
    git \
    vim \
    zlib1g-dev \
    libopenmpi-dev \
    ffmpeg \
    software-properties-common \
    lsb-release \
    sed \
    tmux \
    clangd \
    ripgrep \
    python3-opengl \
    unzip \
    wget \
    luarocks \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy
RUN pip install torch
RUN pip install torchvision
RUN pip install jupyter
RUN pip install notebook
RUN pip install dill
RUN pip install matplotlib

RUN echo "import os" > $HOME/.pdbrc && \
    echo "import sys" >> $HOME/.pdbrc && \
    echo "sys.path.append('/workspaces/python-debugger')" >> $HOME/.pdbrc && \
    echo "with open('/workspaces/python-debugger/helper.py') as file: exec(file.read())" >> $HOME/.pdbrc && \
    echo "alias save save_state(vars())" >> $HOME/.pdbrc

ENV PYTHONPATH=/workspaces/python-debugger:$PYTHONPATH
ENV PYTHONSTARTUP=$HOME/.pdbrc

CMD ["sleep", "infinity"]
