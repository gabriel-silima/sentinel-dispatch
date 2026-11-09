# Requisitos — Aula 06 (09/11/2026)

**Material:** Aula 06 — O Colete à Prova de Balas do Código  
**Professor:** Prof. Ms. Gustavo Sabino  
**Curso:** Técnico em Defesa Cibernética — SENAC Goiás / PMGO  
**Atividade:** Desafio Tático PM-GO — O Despachador Inquebrável (slides 11–14).

## Escopo fiel ao slide 13

| ID | Requisito obrigatório | Evidência no código |
|---|---|---|
| R01 | Repetir a pergunta continuamente | `while True` e `input()` |
| R02 | Converter a entrada em inteiro, dentro de `try` | `int(entrada)` |
| R03 | Tratar `ValueError` com mensagem específica e `continue` | `except ValueError` |
| R04 | Encerrar apenas pelo código especial `999` durante o fluxo normal | `if numero == 999`, `break` |
| R05 | Confirmar o despacho para outros inteiros | `print(f"Viatura {numero} despachada com sucesso.")` |

### Mensagens literais determinadas no slide

- Pergunta: `Qual o prefixo numérico da viatura para despacho?`
- Erro: `Prefixo inválido. O sistema aceita apenas números.`
- Encerramento: `Despacho encerrado. Retornando à base.`
- Sucesso: `Viatura {numero} despachada com sucesso.`

## Procedimento recomendado pelo material

1. Abrir o Google Colab.
2. Criar uma nova célula Python.
3. Construir e executar o laço, aplicando `try`, `int`, `except`, `continue` e `break`.
4. Testar um prefixo numérico, uma entrada textual inválida e `999`.
5. Comparar com o gabarito do slide 14 **após tentar por conta própria**.
6. Registrar evidência real da execução em `docs/screenshots/` (opção de portfólio, não exigência expressa do slide).

## Limites do exercício

Este projeto é uma simulação didática. O uso de `try/except ValueError` impede que **esse erro específico** derrube o fluxo, mas não garante resistência a todas as falhas possíveis (ex.: interrupção externa ou fim da entrada). O exercício pede conversão para `int` e não estabelece intervalo de prefixos nem proibição de negativos: não foram acrescentadas regras além do enunciado.

## Próximas versões

Melhorias de interface, testes automatizados, persistência e validações mais rigorosas são futuras e devem permanecer separadas da implementação original da Aula 06.
