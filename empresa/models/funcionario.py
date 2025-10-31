from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional

@dataclass
class Funcionario:

    _cpf: str
    _pnome: str
    _unome:str
    _data_nasc: date
    _endereco: str = 'Macau-RN'
    _salario: float = 1518.01
    _sexo: str = 'f'
    _cpf_supervisor: Optional[str] = None
    _numero_departamento: Optional[int] = None
    _creat_at: Optional[datetime] = None
    _update_at: Optional[datetime] = None

    # Funcionario -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Funcionario
    @classmethod
    def from_dict(sef, data: dict) -> 'Funcionario':
        return Funcionario (
            data.get('cpf'),
            data.get('pnome'),
            data.get('unome'),
            data.get('data_nasc'),
            data.get('endereco', 'Macau-RN'),
            data.get('salario', 1518.01),
            data.get('sexo', 'f'),
            data.get('cpf_supervisor'),
            data.get('numero_departamento'),
            data.get('creat_at'),
            data.get('update_at')
        )
    
    def __str__(self) -> str:
        return f'Funcionario(cpf={self._cpf}, pnome={self._pnome}, unome={self._unome}, data_nasc={self._data_nasc}, endereco={self._endereco}, salario={self._salario}, sexo={self._sexo}, cpf_supervisor={self._cpf_supervisor}, numero_departamento={self._numero_departamento}, creat_at={self._creat_at}, update_at={self._update_at})'
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf
        self._update_at = datetime.now()

    @property
    def pnome(self) -> str:
        return self._pnome
    
    @pnome.setter
    def pnome(self, pnome: str):
        self._pnome = pnome
        self._update_at = datetime.now()
    

