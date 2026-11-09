"use strict";

const form = document.getElementById("dispatch-form");
const input = document.getElementById("prefix");
const button = document.getElementById("dispatch-button");
const feedback = document.getElementById("feedback");
const resetButton = document.getElementById("reset-button");
const eventLog = document.getElementById("event-log");
const eventCount = document.getElementById("event-count");
const validCount = document.getElementById("valid-count");
const invalidCount = document.getElementById("invalid-count");
const stateValue = document.getElementById("state-value");
const systemTag = document.getElementById("system-tag");

let finished = false;
let valid = 0;
let invalid = 0;
let events = 0;

function renderEvent(result) {
  if (events === 0) eventLog.replaceChildren();
  events += 1;
  const li = document.createElement("li");
  li.className = result.status;
  li.append(document.createTextNode(result.message));
  const time = document.createElement("small");
  time.textContent = new Date().toLocaleTimeString("pt-BR");
  li.append(time);
  eventLog.prepend(li);
  eventCount.textContent = events + (events === 1 ? " EVENT" : " EVENTS");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (finished || button.disabled) return;
  button.disabled = true;
  try {
    const response = await fetch("/api/dispatch", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({prefix: input.value})
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.message || "Falha ao processar.");
    feedback.className = "feedback " + result.status;
    feedback.textContent = result.message;
    renderEvent(result);

    if (result.status === "invalid") {
      invalid += 1;
      invalidCount.textContent = String(invalid).padStart(2, "0");
    }
    if (result.status === "dispatched") {
      valid += 1;
      validCount.textContent = String(valid).padStart(2, "0");
    }
    if (result.status === "finished") {
      finished = true;
      input.disabled = true;
      stateValue.textContent = "CLOSED";
      systemTag.textContent = "SESSION CLOSED";
      resetButton.hidden = false;
    }
    input.value = "";
    if (!finished) input.focus();
  } catch (error) {
    feedback.className = "feedback invalid";
    feedback.textContent = error.message || "Falha ao contactar servidor local.";
  } finally {
    button.disabled = finished;
  }
});

resetButton.addEventListener("click", () => {
  finished = false;
  valid = 0;
  invalid = 0;
  events = 0;
  validCount.textContent = "00";
  invalidCount.textContent = "00";
  eventCount.textContent = "0 EVENTS";
  stateValue.textContent = "ONLINE";
  systemTag.textContent = "SYSTEM READY";
  input.disabled = false;
  button.disabled = false;
  input.value = "";
  feedback.className = "feedback";
  feedback.textContent = "Aguardando entrada do operador.";
  eventLog.replaceChildren();
  const empty = document.createElement("li");
  empty.className = "empty";
  empty.textContent = "Nenhum evento registrado.";
  eventLog.append(empty);
  resetButton.hidden = true;
  input.focus();
});
