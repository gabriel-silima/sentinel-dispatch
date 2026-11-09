# SENTINEL DISPATCH

**Secure Tactical Dispatch Engine**  
*Resilient by Design. Secure by Default.*

Projeto educacional em Python desenvolvido para a **Aula 06 — O Colete à Prova de Balas do Código**, do curso Técnico em Defesa Cibernética (SENAC Goiás / turma PMGO), ministrada pelo Prof. Ms. Gustavo Sabino em 09/11/2026.

## Objetivo

Implementar o desafio **Despachador Inquebrável**, simulando o recebimento de prefixos numéricos de viaturas. O foco é aprender `while True`, `break`, `continue` e `try/except ValueError`, mantendo o programa ativo após erros de digitação.

> **Escopo:** simulador acadêmico; não realiza despachos reais nem se conecta a sistemas policiais.

## Requisitos da atividade (slide 13)

1. Perguntar continuamente: `Qual o prefixo numérico da viatura para despacho?`
2. Converter a entrada com `int()` dentro de `try`.
3. Capturar `ValueError`, exibir `Prefixo inválido. O sistema aceita apenas números.` e usar `continue`.
4. Ao receber `999`, exibir `Despacho encerrado. Retornando à base.` e usar `break`.
5. Para os demais inteiros, exibir `Viatura {numero} despachada com sucesso.`.

## Executar

**No Google Colab:** crie um notebook Python, copie o conteúdo de [src/main.py](src/main.py) para uma nova célula e execute com **Shift + Enter**.

**No terminal (Windows, Linux ou macOS):**

```bash
python src/main.py
```

No Windows, caso o executável seja `py`, use `py src/main.py`.

Não há dependências externas: apenas Python 3.

## Teste manual

Digite estas entradas na sequência:

| Entrada | Saída esperada | Comportamento |
|---|---|---|
| `1234` | `Viatura 1234 despachada com sucesso.` | Continua perguntando |
| `ABC` | `Prefixo inválido. O sistema aceita apenas números.` | Trata o erro e pergunta novamente |
| `999` | `Despacho encerrado. Retornando à base.` | Encerra o laço |

Os resultados acima são **resultados esperados para reprodução pelo aluno**. A publicação do código não comprova, por si só, sua execução no Google Colab. Guarde uma captura real da sua execução em `docs/screenshots/` como evidência.

## Estrutura

```text
sentinel-dispatch/
├── .gitignore
├── LICENSE
├── README.md
├── docs/
│   └── requirements.md
└── src/
    └── main.py
```

## Evolução futura (fora do escopo da Aula 06)

- **v0.2:** testes automatizados e validação aprimorada.
- **v0.3:** interface visual do simulador.
- **v1.0:** arquitetura modular, API e trilha de auditoria para cenários simulados.

As versões futuras não estão implementadas nesta entrega.

## Créditos

- **Desenvolvimento acadêmico:** Gabriel Silveira Lima.
- **Atividade e orientação didática:** Prof. Ms. Gustavo Sabino — SENAC Goiás / PMGO.
- **Data da aula:** 09 de novembro de 2026.

## Licença

Consulte [LICENSE](LICENSE).
