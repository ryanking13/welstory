## How to run

```
virtualenv .env -p=python3.6
call .env/scripts/activate
pip install -r requirements.txt
func host start
```

## Deploy

```
func azure functionapp fetch-app-settings welstory
func azure functionapp publish welstory
```