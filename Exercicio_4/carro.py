class Automovel():

    def __init__(self,cap_dep,quant_comb,consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (self.quant_comb * self.consumo) * 100

    def abastece(self, n_litros):
        if n_litros + self.quant_comb <= self.cap_dep:
            self.quant_comb += n_litros
            return self.autonomia()
        else:
            print("Não é possível abastecer")

    def percorre(self, n_km):
        if self.autonomia() >= (self.quant_comb * self.consumo) * n_km:
            print("É possível")
        else:
            print("Não é possível")
            return self.autonomia()