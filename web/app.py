"""SENTINEL DISPATCH — web simulator (not connected to real dispatch systems)."""
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")
app.json.ensure_ascii = False

PROMPT = "Qual o prefixo numérico da viatura para despacho?"
INVALID_MESSAGE = "Prefixo inválido. O sistema aceita apenas números."
EXIT_MESSAGE = "Despacho encerrado. Retornando à base."


def process_dispatch(entrada: str) -> dict:
    """Replicate the five classroom rules for a single web request.

    The original while True / continue / break remain unchanged in src/main.py.
    HTTP works request by request rather than with an interactive while loop.
    """
    try:
        numero = int(entrada)
    except ValueError:
        return {"status": "invalid", "message": INVALID_MESSAGE, "finished": False}

    if numero == 999:
        return {"status": "finished", "message": EXIT_MESSAGE, "finished": True}

    return {
        "status": "dispatched",
        "message": f"Viatura {numero} despachada com sucesso.",
        "finished": False,
        "prefix": numero,
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "sentinel-dispatch", "mode": "simulation"})


@app.post("/api/dispatch")
def dispatch():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Envie dados no formato JSON."}), 415

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or not isinstance(payload.get("prefix"), str):
        return jsonify({"status": "error", "message": "O campo prefix deve ser texto."}), 400

    if len(payload["prefix"]) > 64:
        return jsonify({"status": "error", "message": "Entrada excede o limite permitido."}), 400

    return jsonify(process_dispatch(payload["prefix"]))


if __name__ == "__main__":
    # Localhost-only by default; never expose this educational app as a real service.
    app.run(host="127.0.0.1", port=5000, debug=False)
