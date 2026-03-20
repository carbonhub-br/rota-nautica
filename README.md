# CarbonHub Maritime Router API

Microserviço de roteamento marítimo usando o grafo AIS do JRC/Eurostat.

## Deploy no Render.com

1. Crie conta em https://render.com (gratuito)
2. New → Web Service → Connect a repository (ou use Deploy from Git)
3. Faça upload destes arquivos num repositório GitHub
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free
5. Após deploy, anote a URL (ex: `https://carbonhub-maritime-router.onrender.com`)

## Endpoint

```
GET /route?flon={lon}&flat={lat}&tlon={lon}&tlat={lat}
```

Exemplo:
```
GET /route?flon=-46.3&flat=-23.95&tlon=101.4&tlat=3.0
```

Resposta:
```json
{
  "success": true,
  "km": 16642.4,
  "nm": 8986.2,
  "coords": [[-24.3, -46.3], ...],
  "points": 61
}
```
