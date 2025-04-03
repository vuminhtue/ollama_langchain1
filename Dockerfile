FROM python:3.10.16

WORKDIR /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENV OLLAMA_BASE_URL="/ollama"

COPY / ./
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
