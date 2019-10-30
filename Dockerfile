FROM python:3

RUN git clone https://github.com/NicoBeast98/TaTeTI.git

WORKDIR /TaTeTI

RUN pip install -r requirements.txt

CMD ["python3", "./test_tateti.py"]