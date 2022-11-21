# online_shop

## Execute rabbitMQ with Docker
### 1. docker pull rabbitmq
### 2.  docker run -it --rm  --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
##### 3. User and Pass -> guest
### Start celery: celery -A myshop worker -l info
### Monitor Celery with Flower: celery -A myshop flower