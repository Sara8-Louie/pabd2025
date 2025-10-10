class funcionario:

    __slots__ = ['_nome', '_cpf', '_salario']
    
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    @property
    def nome (self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def cpf (self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf 

    @property
    def salario (self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario