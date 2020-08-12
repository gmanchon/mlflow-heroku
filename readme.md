
# conf

heroku provides the port to listen on in the `$PORT` env var
`--host 0.0.0.0` tells mlflow to listen to the network and not only the local machine

``` bash
mlflow ui -p $PORT --host 0.0.0.0
```

# setup

``` bash
heroku create APP_NAME --region eu
heroku ps:scale web=1
```
