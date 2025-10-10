from historico import Historico

class Conta:
    def __init__(self,cliente,agencia,numero,pix,saldo):
        self.cliente = cliente #agregacao
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self._saldo = saldo
        self.historico = Historico() #composição
        self._total_contas += 1

    @property
    def total_contas(self):
        return self._total_contas

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo!')
        else:
            self._saldo = saldo
    
    ## Não se aplica nesse caso
    # def set_saldo(self, saldo):
    #   self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append(f'✅ Depósito de R$ {valor:.2f}')

    def saca(self, valor):
        if(self._saldo < valor):
           self.historico.transacoes.append(f'❌ Saldo insulficiente. Saque: R$ {valor:.2f} - Saldo: R$ {self._saldo:.2f}')
           return False
        else:
         self._saldo -= valor
         self.historico.transacoes.append(f'⛔ Saque de R$ {valor:.2f}')
        return True

    def extrato(self):
        self.historico.transacoes.append(f'❗ Extrato. Saldo R$ {self._saldo:.2f}')
        print(f'Titular:{self.cliente.nome}\n{self.titular}\nAgência: {self.agencia}\nNúmero: {self.numero}\nPIX: {self.pix}\nSaldo: {self._saldo:.2f}\n')

    def transfere(self, destino, valor):
        self.historico.transacoes.append(f'❗ Transferência para {destino.cliente.nome}')
        if(self.saca(valor)):
            destino.deposita(valor)
            return True
        else:
            return False