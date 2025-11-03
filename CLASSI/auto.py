from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, carburante: str, porte: int) -> None:
        super().__init__(marca, modello, carburante)
        self.porte = porte

    def descrizione(self) -> str:
        return f"Auto:\n{super().descrizione()}\nNumero porte: {self.porte}"