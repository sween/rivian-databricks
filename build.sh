docker build -t rivian-databricks .
docker image tag rivian-databricks sween/rivian-databricks:latest
docker push sween/rivian-databricks:latest