### for Birthe
docker build . -t image-resize
docker run -d -p 8000:80 image-resize

airflow ping to webserver ---> python-ping.py == task


######

docker build . -t philcloudwalker/image-downsizing:v7



###---- infos for phil ---#
docker push philcloudwalker/image-downsizing:v7

aws-prefix: image-resize-v7-1-phd

#test local
docker run -it -p 8000:80 philcloudwalker/image-downsizing:v4

----
Wo ist der Load Balancer?
cluster --> servcie --> Target Group Name --> Load Balancer --> DNS

Was sind die Gründe für nen Abbruch?
- Health checks:
        cluster ---> servcie --> events
    - anpassen bei Loadbalancer --> Steady state when es funktioniert
- konte kein file erstellen --> Docker file anpassen (noch nicht probiert)
https://gitlab.com/testdriven/flask-tdd-docker/-/blob/aws-fargate/Dockerfile
    - möglicher Gund: voreingestellte sh command in der container definition --> fail :D


Wo sehe ich Metriken?
cluster --> service --> Metrics