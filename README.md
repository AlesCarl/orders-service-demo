# orders-service-demo

Piccolo servizio ordini in Python con FastAPI (dati in memoria), pensato come
repo di prova per fare pratica con il flusso Git di un team: branch, PR,
review, CI e merge.

## Comandi

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

## Flusso di lavoro

- `main` = codice rilasciato
- `develop` = integrazione
- i branch di lavoro si chiamano `feature/ORD-123-descrizione` e partono da `develop`
- i messaggi di commit iniziano col ticket, es. `ORD-123: aggiunge validazione`
- ogni modifica arriva su `develop` tramite Pull Request con CI verde

## Ticket da svolgere

**ORD-142**: aggiungere `GET /health` che risponde 200 con `{"status":"UP"}`
