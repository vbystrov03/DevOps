# Установка k8s 
## Инициализация первой ноды 
kubeadm init --conig pathtoconfig

## Создание токена для подключения новых нод 
kubeadm token create --print-join-command

## Установка CNI (сетевого плагина)
kubectl apply -f https://projectcalico.docs.tigera.io/manifests/calico.yaml
