'''
  BaseDAO
  Classe abstrata base para DAOs (Data Access Objects).
  Operações CRUD genéricas
'''

from abc import ABC, abstractmethod # Vai obrigar quem herdar da base pao a implementar os métodos abstratos
from typing import List, Optional, TypeVar, Generic
from supabase import Client 

# TypeVar - tornar a classe genérica
T = TypeVar('T')  # Tipo genérico para as entidades que o DAO irá manipular

class BaseDAO(ABC, Generic[T]):
  
  def __init__(self, client: Client, table_name: str):
    self.client = client
    self.table_name = table_name
    
    
  # Do formato JSON (dict) para o formato model (classe)
  @abstractmethod 
  def to_model (self,data: dict) -> T: # Forçando o "seu filho" a implementar o método to_model e vai ter que retornar um tipo de dado
    pass
  
  # Do modelo de dados (T) para o formato JSON (dict)
  @abstractmethod 
  def to_dict (self, model: T) -> dict:
    pass
  
  ### Create
  
  ### Read
  
  # Retorna todos os valores de uma tabela
  def read_all(self) -> List[T]:
    try:
      response = self._client.table(self._table_name).select('*').execute()
      if response.data:
        return[self.to_model(item) for item in response.data]
      return []
    except Exception as e:
      print(f"Erro ao buscar todos os registros: {e}")
      return []
  
  # Update
  
  # delete
  
  
  