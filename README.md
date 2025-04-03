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
