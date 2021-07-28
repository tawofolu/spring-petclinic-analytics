## Deploying on Kubernetes
PETCLINIC_ANALYTICS_IMAGE_VERSION=`date "+%Y%m%d.%H%M"`
docker build -t oawofolu/spring-petclinic-dashboard:${PETCLINIC_ANALYTICS_IMAGE_VERSION} .
docker tag oawofolu/spring-petclinic-dashboard:${PETCLINIC_ANALYTICS_IMAGE_VERSION} oawofolu/spring-petclinic-dashboard
docker push oawofolu/spring-petclinic-dashboard
kubectl delete svc petclinic-app-dashboard --ignore-not-found=true
kubectl delete deploy petclinic-app-dashboard --ignore-not-found=true
kubectl create deployment petclinic-app-dashboard --image=oawofolu/spring-petclinic-dashboard:latest
kubectl port-forward deploy/petclinic-app-dashboard 8050

#kubectl expose deployment/petclinic-app-dashboard --name petclinic-app-dashboard --port=8050 --type=ClusterIP
