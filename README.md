# Esempi per Corso GitHub Copilot

## 1. Completamento Inline (Ghost Text)
Scrivi una funzione Python che calcoli la somma di tutti i numeri pari in una lista e lascia Copilot suggerire il completamento:

```python
def somma_pari(lista):
    # Copilot suggerirà: return sum(x for x in lista if x % 2 == 0)
```

## 2. Completamento di Blocchi di Codice
Scrivi il nome della funzione e la docstring per calcolare la deviazione standard di una lista di numeri:

```python
def deviazione_standard(lista):
    """
    Calcola la deviazione standard di una lista di numeri.
    """
    # Copilot suggerirà il corpo della funzione
```

## 3. Comandi Rapidi `/` in Copilot Chat
Nel contesto di **GitHub Copilot Chat**, il simbolo `/` viene utilizzato per attivare comandi speciali che aiutano nella scrittura, spiegazione e correzione del codice. Esempi comuni:

- `/explain` Spiega il codice selezionato o incollato.
- `/tests` Genera test automatici per una funzione o classe.
- `/fix` Suggerisce correzioni per codice che presenta errori.

Questi comandi vanno scritti direttamente nella chat Copilot, seguiti dal codice o dalla richiesta desiderata.

## 4. Completamento di File Interi
Scrivi solo l’intestazione di una classe che gestisce una rubrica di contatti e lascia che Copilot suggerisca il resto:

```python
class RubricaContatti:
    """
    Classe per gestire una rubrica di contatti con ricerca e salvataggio su file.
    """
```

---

Questi esempi mostrano funzionalità base di GitHub Copilot utili durante un corso.

## 5. Differenza tra Completamento Inline e Copilot Chat

### Completamento Inline (Ghost Text)
- **Cos’è:** Suggerimenti che appaiono direttamente nel codice mentre scrivi (testo grigio chiaro).
- **Come si usa:** Premi `Tab` per accettare il suggerimento.
- **Scopo:** Ideale per completare rapidamente funzioni, variabili o blocchi di codice mentre lavori.
- **Tasto rapido:** `Ctrl+I` (o `Tab` quando il suggerimento è visibile).

### Copilot Chat
- **Cos’è:** Una chat laterale dove puoi porre domande in linguaggio naturale, chiedere spiegazioni, generare codice, correggere errori, o ottenere suggerimenti più articolati.
- **Come si usa:** Apri la chat (di solito dal pannello laterale dell’editor) e scrivi richieste come “Spiega questa funzione” o “Genera test per questa classe”.
- **Scopo:** Utile per ricevere spiegazioni dettagliate, refactoring, generazione di documentazione, o supporto su più file.
- **Tasto rapido:** `Ctrl+Alt+I` (o icona Copilot Chat nella barra laterale).

### Esempi di utilizzo Copilot Chat

#### 1. Spiegare una funzione
```
/explain
```
Scrivi questo comando nella chat seguito dal codice da spiegare. Copilot fornirà una spiegazione dettagliata.

#### 2. Generare test automatici
```
/tests
```
Incolla la funzione per cui vuoi i test e Copilot genererà i test unitari.

#### 3. Correggere errori
```
/fix
```
Incolla il codice che dà errore e Copilot suggerirà una correzione.

#### 4. Chiedere suggerimenti o alternative
Puoi scrivere domande come:
```
Come posso ottimizzare questa funzione?
Qual è la differenza tra una lista e un set in Python?
```

---

**In sintesi:**  
- Il completamento inline è veloce e contestuale, ideale per suggerimenti rapidi mentre scrivi codice.
- Copilot Chat è più adatto per richieste complesse, spiegazioni, generazione di test, refactoring e supporto interattivo.

#### Edit Mode vs Agent Mode (at a glance)

| Aspect         | ✏️ Edit Mode                      | 👩‍🚀 Agent Mode                                                                    |
| -------------- | --------------------------------- | -------------------------------------------------------------------------------- |
| Context scope  | Only the files you explicitly add | May read/add additional files & surfaces as needed                               |
| Self‑review    | Minimal (you drive iteration)     | Built‑in feedback & retry loop on errors/failures                                |
| Change scope   | Highly scoped & surgical          | Broader; may touch related layers for consistency                                |
| When to choose | You know exactly what to change   | Goal is broader or uncertain; requires exploration                               |
| Tool calling   | None (you run commands manually)  | Can invoke tools (read/edit files, run commands, inspect terminal & test output) |