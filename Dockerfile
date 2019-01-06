FROM python:3.6
ADD valhalla.py /
RUN python3 -m pip install -U discord.py
CMD exec python3.6 valhalla.py > server.log 2>&1
