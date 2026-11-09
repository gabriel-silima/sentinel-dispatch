"""Tests for the Sentinel Dispatch web simulator."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app, process_dispatch


class WebDispatchTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_html_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Dispatch", response.data)

    def test_healthy(self):
        self.assertEqual(self.client.get("/api/health").json["status"], "ok")

    def test_valid_prefix(self):
        result = self.client.post("/api/dispatch", json={"prefix": "810605"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json["message"], "Viatura 810605 despachada com sucesso.")

    def test_text_value_error(self):
        result = self.client.post("/api/dispatch", json={"prefix": "VIATURA"})
        self.assertEqual(result.json["status"], "invalid")
        self.assertEqual(result.json["message"], "Prefixo inválido. O sistema aceita apenas números.")

    def test_decimal_value_error(self):
        self.assertEqual(process_dispatch("8.13782")["status"], "invalid")

    def test_999_break_equivalent(self):
        result = self.client.post("/api/dispatch", json={"prefix": "999"})
        self.assertTrue(result.json["finished"])
        self.assertEqual(result.json["message"], "Despacho encerrado. Retornando à base.")

    def test_wrong_payload(self):
        result = self.client.post("/api/dispatch", json={"prefix": 123})
        self.assertEqual(result.status_code, 400)

    def test_input_limit(self):
        result = self.client.post("/api/dispatch", json={"prefix": "1" * 65})
        self.assertEqual(result.status_code, 400)


if __name__ == "__main__":
    unittest.main()
