# Kaisar USERBOT
FROM jokokendil/ambohju: buster

#
# Kaisar
#
RUN git clone -b Kaisar-userbot https://github.com/kenkannih/Kaisar-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/kenkannih/Kaisar-userbot/Kaisar-userbot/requirements.txt

CMD ["python3","-m","userbot"]
