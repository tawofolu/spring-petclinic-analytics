## Deploying on Kubernetes

docker build -t oawofolu/spring-petclinic-dashboard:1.0 .
docker push oawofolu/spring-petclinic-dashboard:1.0
kubectl create deployment petclinic-app-dashboard --image=oawofolu/spring-petclinic-dashboard:1.0 --replicas=2
kubectl expose deployment/petclinic-app-dashboard --name petclinic-app --port=8080 --type=ClusterIP