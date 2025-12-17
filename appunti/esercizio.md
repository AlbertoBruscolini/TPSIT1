# Git TPSIT

##  Spiegazione
In questo esercizio ho imparato a usare **Git** e **GitHub** per gestire un progetto Python con più file e branch.

Il progetto si chiama **TPSITI** e contiene tre file principali all’interno della cartella `CLASSI`:
- `veicolo.py`
- `auto.py`
- `moto.py`
# Descrizione dell'ultimo lavoro versionato su GitHub


## attività svolte

- **Creazione repository**: inizializzato `git`, creato repository remoto su GitHub.
- **Branching**: creato un branch `moto` per lo sviluppo della classe `Moto`, poi fuso in `main` dopo i test.
- **Correzione di errori**: ho annullato un commit errato usando `git reset` e sincronizzato con `push --force-with-lease`.

### Struttura principale del progetto

`CLASSI/`

- `auto.py` — implementa la classe Auto
- `veicolo.py` — classe base Veicolo
- `moto.py` — classe Moto (aggiunta sul branch `moto` e poi integrata)

## Dettagli operativi (comandi principali usati)

1. Configurazione autore e creazione cartelle

```bash
git config --global user.name "AlbertoBruscolini"
git config --global user.email "alberto.bruscolini@studenti.isissgobetti.it"
mkdir CLASSI
```

2. Aggiunta, commit e push

```bash
git add CLASSI/
git commit -m "Aggiungo le classi base"
git push origin main
```

3. Creazione branch e push remoto del branch

```bash
git checkout -b moto
git add CLASSI/moto.py
git commit -m "Aggiunta classe Moto"
git push -u origin moto
```

4. Merge in `main` e sincronizzazione

```bash
git checkout main
git merge moto
git push
```

5. Ripristino di un commit errato 

```bash
git reset --hard HEAD~1
git push --force-with-lease
```

## Note aggiuntive

Spiego alcune decisioni prese durante il lavoro:[^1][^2]

[^1]: Ho usato il reset con `--hard` solo dopo essermi assicurato che la versione corretta fosse salvata altrove; l'uso di `--hard` può causare perdita di dati locali.
[^2]: Per evitare conflitti con altri collaboratori, è preferibile usare `git revert` quando si lavora in team.

## Checklist — 3 domande (spuntare la risposta corretta)

1. Hai effettuato il push dell'ultimo commit sul repository remoto?
	- [ ] Sì
	- [ ] No

2. Hai creato e testato le modifiche sul branch `moto` prima del merge?
	- [ ] Sì
	- [ ] No

3. Hai aggiornato il `README.md` con istruzioni per eseguire il progetto?
	- [ ] Sì
	- [ ] No
