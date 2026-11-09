# Sentinel Dispatch — Web Control Room v0.2

Esta é a evolução web do **Sentinel Dispatch**, um projeto autoral de portfólio acadêmico. O protótipo combina HTML, CSS, JavaScript e um backend Python/Flask.

> **Simulação de ensino.** Não conecta, rastreia ou despacha viaturas reais. Não utilize identificadores ou dados operacionais sensíveis.

## Preservação da Aula 06

O código original do professor continua disponível, **sem alterações**, em [../src/main.py](../src/main.py) e no [notebook executado](../notebooks/Sentinel_Dispatch_Aula06.ipynb). Nele, `while True`, `continue` e `break` permanecem visíveis conforme o exercício.

A web funciona por **requisições HTTP**, não por um `while True` dentro do servidor. Cada envio do formulário corresponde a uma iteração: o backend utiliza `try/int/except ValueError`; o JavaScript repete a solicitação após entradas inválidas e encerra a sessão visual com `999`. Assim, o comportamento das **cinco regras** é preservado, sem bloquear o servidor num laço infinito.

| Aula 06 | Comportamento web |
|---|---|
| Perguntar continuamente | Formulário permanece disponível após cada envio |
| Converter com `int()` em `try` | `process_dispatch` no backend Python |
| `except ValueError` e `continue` | Exibe mensagem literal e permite novo envio |
| `999` e `break` | Exibe mensagem literal e desabilita formulário da sessão |
| Confirmar despacho | Exibe `Viatura {numero} despachada com sucesso.` |

## Instalação no Windows (PowerShell)

Execute a partir da raiz do repositório clonado:

```powershell
cd web
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Se a execução de scripts estiver bloqueada, não é necessário mudar a política do sistema: rode diretamente ` .\.venv\Scripts\python.exe -m pip install -r requirements.txt ` e depois ` .\.venv\Scripts\python.exe app.py `.

Abra **http://127.0.0.1:5000**. Para encerrar o servidor, pressione **Ctrl+C** no terminal.

## Instalação no Linux / macOS

```bash
cd web
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

## Testes

Com o ambiente Python ativado e dentro da pasta `web`:

```bash
python -m unittest discover -s tests -v
```

Os testes cobrem a renderização HTML, saúde da API, entrada válida, texto inválido, decimal inválido, código `999` e payloads incorretos.

## Endpoints locais

- `GET /` — painel HTML.
- `GET /api/health` — status do protótipo.
- `POST /api/dispatch` — recebe JSON `{"prefix":"810605"}` e devolve o resultado simulado.

## Segurança e limites

- O servidor inicia em **127.0.0.1**, com `debug=False`; não foi preparado para implantação pública.
- O backend exige JSON e texto com até 64 caracteres, convertendo os dados com `int()`.
- A interface registra eventos apenas em memória do navegador, sem persistência.
- O encerramento por `999` é controlado **na sessão do navegador**. A API é sem estado: não implementa controle de acesso, autenticação ou bloqueio permanente.
- Não há banco de dados, operações institucionais nem despacho real.

## Autoria e créditos

**Sentinel Dispatch** — conceito, identidade visual e projeto de portfólio desenvolvido em colaboração com assistência de IA para Gabriel Silveira Lima. Atividade-base da **Aula 06**, Prof. Ms. Gustavo Sabino, curso Técnico em Defesa Cibernética — SENAC Goiás/PMGO, 09/11/2026. A aparência e a organização da interface web são expansão do projeto, não conteúdo exigido pelo professor.

## Roadmap

- v0.1: exercício Python original — preservado em `main`.
- v0.2: dashboard web e API de simulação — desenvolvimento na branch `develop`.
- Futuro: melhorias de acessibilidade, segurança de sessão, testes de integração e documentação técnica.

**Estado de validação:** código e testes versionados; a execução local do servidor web ainda precisa ser confirmada no ambiente do aluno.
