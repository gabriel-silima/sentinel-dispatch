# Evidência de execução — Aula 06

- **Projeto:** SENTINEL DISPATCH v0.1
- **Data:** 09/11/2026
- **Ambiente:** Google Colab (Python 3)
- **Material de referência:** Aula 06 — O Colete à Prova de Balas do Código, Prof. Ms. Gustavo Sabino, SENAC/PMGO.
- **Situação:** execução concluída pelo aluno e conferida visualmente a partir de captura de tela compartilhada em 09/11/2026.

## Testes observados na captura

| Entrada | Comportamento observado | Resultado |
|---|---|---|
| `810605` | `Viatura 810605 despachada com sucesso.` | Aprovado |
| `8.16578` | `Prefixo inválido. O sistema aceita apenas números.` | Aprovado |
| `693786` | `Viatura 693786 despachada com sucesso.` | Aprovado |
| `8.13782` | `Prefixo inválido. O sistema aceita apenas números.` | Aprovado |
| `999` | `Despacho encerrado. Retornando à base.` | Aprovado |

A captura mostra a célula do Colab concluída, sem traceback. Os dados são entradas de **simulação didática**, não registros de despachos reais.

## Correspondência com as regras do professor

1. `while True`: a pergunta se repete após cada entrada.
2. `int()` dentro de `try`: aceita os prefixos inteiros digitados.
3. `except ValueError` e `continue`: trata entradas com ponto e segue para próxima solicitação.
4. `break` para `999`: encerra o laço de forma controlada.
5. `print()` formatado: confirma o despacho simulado com o prefixo.

**Conclusão:** os cinco requisitos didáticos previstos no slide 13 foram demonstrados na execução apresentada.

## Artefatos de evidência a anexar

- `docs/screenshots/aula06-colab-execution.png` — captura original do Colab, ainda não anexada ao repositório.
- `notebooks/Sentinel_Dispatch_Aula06.ipynb` — notebook original exportado do Colab, ainda não anexado ao repositório.

O notebook original deve ser exportado via **Arquivo → Fazer download → Fazer download do .ipynb**, sem recriar artificialmente os resultados. A captura pode ser anexada via **GitHub → Add file → Upload files**.

Este registro documenta apenas a execução observada; não atesta aprovação formal do professor nem robustez contra todas as categorias de exceção.
