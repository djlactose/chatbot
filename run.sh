if [ ! -f /mnt/ggml-gpt4all-j.bin ]
then
    wget https://gpt4all.io/models/ggml-gpt4all-j.bin
fi
python3 /root/bin/app.py