#Following the directions from https://gpt4all.io/index.html
FROM ubuntu

EXPOSE 5000

VOLUME /mnt

COPY templates/ /root/bin/templates/
COPY app.py /root/bin/
COPY run.sh /root/bin/

RUN apt-get update && \
apt-get install -y wget python3 python3-pip cmake git build-essential && \
pip install flask && \
cd /tmp/ && \
git clone --recurse-submodules https://github.com/nomic-ai/gpt4all-chat && \
cd gpt4all-chat/ggml && \
mkdir build && \
cd build && \
cmake .. && \ 
cmake --build . --parallel

ENTRYPOINT /root/bin/run.sh