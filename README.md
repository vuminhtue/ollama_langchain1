Procedure:

1. Run Ollama as backend docker:
https://hub.docker.com/r/ollama/ollama

Steps:
  - docker pull ollama/ollama
  - docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

Check by:
  - docker ps
  - docker exec -it ollama ollama bash
  - docker exec -it ollama ollama pull llama3.2:1b

2. After that, install the requirement and run streamlit:
  - pip install -r requirement.txt
  - streamlit run app.py

This runs fine for me

3. I create a docker container called chatapp:
  - docker build -t chatapp .

The docker image is created from the Dockerfile
However, the built container could not connect to ollama backend:
  - docker run -p 8501:8501 -name chatapp chatapp

Some approach such as docker network or link didnt work
