# Rivian Databricks
Supporting assets for Rivian Databricks Lakehouse

<img src="https://github.com/sween/rivian-databricks/raw/main/assets/rivian-databricks.png" alt="Aspiring Brick Builder">

Create a namespace and add your Rivian Credentials as a secret:

```
kubectl create ns rivian
kubectl create secret generic rivian-user-pass -n rivian \
    --from-literal=rivian_username='ron.sweeney+api@hotmale.com' \
    --from-literal=rivian_password='12345' # same as your luggage

kubectl create secret generic aws-creds -n rivian \
    --from-literal=aws_access_key_id='AKIA.....' \
    --from-literal=aws_secret_access_key='12345' \ # same as your luggage
    --from-literal=aws_default_region='us-east-2'
```

Apply the Job

```
kubectl apply -f deploy/cronjob.yaml -n rivian
```

More Documentation and Errata over @ [Deez Watts - A Rivian Data Adventure](https://www.deezwatts.com)

## Props
The Mace [the-mace/rivian-python-api](https://github.com/the-mace/rivian-python-api)  

kaedenbrinkman [kaedenbrinkman/rivian-api](https://github.com/kaedenbrinkman/rivian-api)  


## Author
Ron Sweeney [sween](https://www.github.com/sween)

