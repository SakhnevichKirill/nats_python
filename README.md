# nats_js
для запуска nats + два микросервиса прописать:
```
docker compose up
```

чтобы потестить 2 воркера:
```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r ./consumer/requirements.txt
python -m pip install -r ./publisher/requirements.txt
```