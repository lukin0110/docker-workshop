# Commands

## Docker Compose
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

## Docker Machine
```bash
$ docker-machine create workshop
```

```bash
$ eval $(docker-machine env workshop)
```

```bash
$ eval $(docker-machine env --unset)
```

```bash
$ docker-machine create "WorkshopEC2" \
    --driver amazonec2 \
    --amazonec2-vpc-id "vpc-4f312228" \
    --amazonec2-region "eu-west-1" \
    --amazonec2-instance-type "t2.micro" \
    --amazonec2-access-key "AK***" \
    --amazonec2-secret-key "oC7****"
```

## Alt flask run

```bash
EXPOSE 5000
ENV FLASK_APP=/usr/src/app/app.py

# run the application
#CMD ["flask", "run"]
```
