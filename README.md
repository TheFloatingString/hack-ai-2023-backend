# backend

To install dependencies:

```bash
pip install -r requirements.txt
```

To run:

```bash
uvicorn main:app --reload
```

Sample request:

```curl
curl -XPOST http://127.0.0.1:8000/api/story -d "{\"name\": \"Bao\", \"modifier\": \"x\", \"narration\": \"x\", \"topic\": \"what is energy?\", \"character_environment\":\"Harry Potter universe\"}" -H "Content-type: application/json"
```

Go to port `8000`
