# Backend

<<<<<<< HEAD
__IMPORTANT!__ You must create `token.txt` in the project's root directory first. This file will contain your Facebook API token and will be used by `backmt.py`.

## Run without Docker

1. Install dependencies using 
```
> pip install -r requirements.txt
```

2. Run the Flask server using
```
> python back.py
```

## Run with Docker

1. Build the Docker image using
```
> docker build -t asr/back .
```

2. Run a Docker container using
```
> docker run --rm -it -p 5000:5000 asr/back
```
=======
1. Paste your token in token.txt
2. run this by "python back.py"
>>>>>>> 781dfeec69140575d3a039ed9c51c76584a85448
