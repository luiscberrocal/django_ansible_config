
docker rmi -f $(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'rec_promoter_app')

