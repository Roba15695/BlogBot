FROM python:3.9

RUN useradd -m -u 1000 user

WORKDIR /app

ENV PINECONE_API_KEY="1a635349-ea24-4a2d-a056-601e82d46648"
ENV PYTHONUNBUFFERED=1

COPY --chown=user ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install --upgrade sentence_transformers

RUN pip install --upgrade langchain

COPY --chown=user . /app

CMD ["gunicorn", "app:app","-b","0.0.0.0:7860"]

