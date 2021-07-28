PETCLINIC_ANALYTICS_IMAGE_VERSION=`date "+%Y%m%d.%H%M"`
docker build -t oawofolu/petclinic-analytics:0.30 .
docker tag oawofolu/petclinic-analytics:0.30 oawofolu/petclinic-analytics
docker push oawofolu/petclinic-analytics:0.30
docker push oawofolu/petclinic-analytics:0.30
kubectl delete svc petclinic-app-analytics --ignore-not-found=true
kubectl delete deploy petclinic-app-analytics --ignore-not-found=true
kubectl create deployment petclinic-app-analytics --image=oawofolu/petclinic-analytics:0.30
#kubectl port-forward deploy/petclinic-app-analytics 8050
