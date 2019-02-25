# Commands

```bash
$ docker-compose build
```

```bash
$ docker-compose run -d redis
```

```bash
$ docker-compose up app 
```

```bash
$ docker-compose run app /bin/bash
```

## Alt flask run

```bash
EXPOSE 5000
ENV FLASK_APP=/usr/src/app/app.py

# run the application
#CMD ["flask", "run"]
```
