# Correr Proyecto con Docker
    Pasos a ejecutar:
        - docker build -t fastapi-fapro .
        - docker run -p 8000:8000 fastapi-fapro
# Correr Proyecto sin Docker

### Cree virtulenv
    primero instale virtualenv
        pip install virtualenv

    crear virtualenv
        virtualenv entorno
    Activar entorno virtual en powershell
        .\entorno\Scripts\activate.ps1
    Activar entorno virtual en terminal de windows
        .\entorno\Scripts\activate.bat


### Instalar librerias


pip3 install -r local.txt

pip install -r local.txt

## Correr app

uvicorn main:app --host 0.0.0.0 --port 8000


En el caso de querer ejecutar fastapi con debug esta el launch.json configurado