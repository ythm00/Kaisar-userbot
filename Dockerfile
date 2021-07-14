# Kaisar USERBOT
FROM irhamfadzillah/cyber:buster

#
# Kaisar
#
RUN git clone -b Kaisar-userbot https://github.com/ythm00/Kaisar-userbot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#RUN pip install --upgrade pip setuptools

#Install python requirements
#RUN pip3 install -r https://raw.githubusercontent.com/kenkansaja/ythm00/Kaisar-userbot/requirements.txt

EXPOSE 443 80

CMD ["python3","-m","userbot"]
