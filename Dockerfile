FROM python

WORKDIR /monApp

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug"]

# UTILISATION : docker build --tag python-flask .
# PUIS : docker run -it -v /mylocalpath:/monApp -p 5000:5000 python-flask