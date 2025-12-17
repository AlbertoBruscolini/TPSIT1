# 💻 Relazione Git TPSITI

## 🧩 Introduzione
In questo esercizio ho imparato a usare **Git** e **GitHub** per gestire un progetto Python con più file e branch.

Il progetto si chiama **TPSITI** e contiene tre file principali all’interno della cartella `CLASSI`:
- `veicolo.py`
- `auto.py`
- `moto.py`

---

## 🪜 Passaggi svolti

### 1️⃣ Creazione del progetto e configurazione iniziale
Ho creato una nuova cartella chiamata `TPSITI` e all’interno di essa una sottocartella `CLASSI`.

```bash
mkdir CLASSI
git config --global user.name "AlbertoBruscolini"
git config --global user.email "alberto.bruscolini@studenti.isissgobetti.it"
```

Ho poi verificato il collegamento al repository remoto su GitHub:

```bash
git remote -v
```

Tutto risultava corretto: il repository remoto puntava a  
`https://github.com/AlbertoBruscolini/TPSITI1.git`.

---

### 2️⃣ Aggiunta dei primi file e primo commit
Ho creato i file `veicolo.py` e `auto.py` dentro `CLASSI/`, poi li ho aggiunti e committati.

```bash
git add *
git commit -m "Aggiungo Classi"
git push
```

✅ Questo ha caricato i file sul branch principale (`main`) su GitHub.

---

### 3️⃣ Creazione di un nuovo branch per “Moto”
Ho creato un branch dedicato per aggiungere la classe `Moto`:

```bash
git checkout -b moto
```

Ho poi aggiunto e committato il nuovo file:

```bash
git add *
git commit -m "Aggiunto Moto"
```

Quando ho provato a fare il push, inizialmente ho ricevuto un errore (“no upstream branch”), ma poi ho risolto con:

```bash
git push -u origin moto
```

✅ Questo ha creato il branch remoto `moto` su GitHub.

---

### 4️⃣ Merge e sincronizzazione
Dopo aver verificato che tutto funzionava sul branch `moto`, sono tornato su `main` e ho unito le modifiche:

```bash
git checkout main
git merge moto
git push
```

✅ Ora anche il branch `main` contiene il file `moto.py`.

---

### 5️⃣ Correzione di un commit errato
Durante le prove, ho fatto per sbaglio un commit errato.  
Per eliminarlo ho usato:

```bash
git reset --hard HEAD~1
git push --force-with-lease
```

✅ Così ho annullato l’ultimo commit sia in locale che su remoto.

---

## 🧠 Cosa ho imparato
- Come creare e collegare un repository locale a GitHub.
- Come aggiungere, committare e pushare modifiche.
- Come creare e gestire branch separati.
- Come risolvere errori e annullare commit errati.
- Come unire rami diversi con `merge`.

---

## ✅ Stato finale del progetto
Alla fine, il branch `main` contiene tutti e tre i file:

```
CLASSI/
 ├── auto.py
 ├── veicolo.py
 └── moto.py
```

Tutto è sincronizzato con GitHub e il progetto è completo. 
