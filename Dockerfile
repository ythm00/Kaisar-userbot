# kaisar userbot
FROM kenkan123/dahlah:buster

#
# LORD
#
RUN git clone -b kaisar-userbot https://github.com/kenkannih/kaisar-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/kenkannih/kaisar-userbot/kaisar-userbot/requirements.txt

CMD ["python3","-m","userbot"]
