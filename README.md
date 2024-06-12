<h1> 
    🎙️ Recognize Speach Service
</h1>

<h3>
    Recognize Speach Service - это сервис для распознавания речи в видео
</h3>



</br>



<h2>
    🛠️ Инструменты:
</h2>

- Python
- FastAPI
- SpeechRecognition
- Docker



</br>



<h2>
    🚀 Зпуск приложения:
</h2>

- Зпускаем локально:
    - устанавливаем Python 3.8.10
    - `git clone https://github.com/ElishaFlacon/recognize-speech-service.git`
    - `cd recognize-speech-service`
    - `cp .env-example .env`
    - `cp .env-example .env.prod`
    - `python -m venv <venv_name>`
    - `<venv_name>/Scripts/activate` (windows) или `source <venv_name>/Scripts/activate` (linux)
    - `pip install -r ./requirements.txt`

- Зпускаем через Docker:
    - устанавливаем Docker
    - добавляем в конфиг Docker зеркала, <a href="https://dockerhub.timeweb.cloud/">тут гайд</a>
    - `git clone https://github.com/ElishaFlacon/recognize-speech-service.git`
    - `cd recognize-speech-service`
    - `cp .env-example .env`
    - `cp .env-example .env.prod`
    - `docker-compose build`
    - `docker-compose up`
    - также для этого проекта есть <a href="https://hub.docker.com/r/elishaflacon/recognize-speech-service">docker image</a>
<h3>
    Запускаем, не работет, ура! 🗿🚬
</h3>



</br>



<h2>
    ⚡ Немного дополнительной информации:
</h2>

- Env app mode `PROD` или `DEV`
- Документация `localhost:8000/docs`
- P.S. Все баги и недочеты - это фичи





<br/>
<br/>
<br/>
<br/>
<br/>
<br/>





<p align="center">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=d179b8&height=64&section=footer"/>
</p>
