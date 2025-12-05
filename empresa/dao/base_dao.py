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
  def to_model(self, data: dict) -> T: # Forçando o "seu filho" a implementar o método to_model e vai ter que retornar um tipo de dado
    pass
  
  # Do modelo de dados (T) para o formato JSON (dict)
  @abstractmethod 
  def to_dict(self, model: T) -> dict:
    pass
  
  ### Create 
  def create(self, model: T) -> Optional[T]: #recebe um modelo genérico T
        try:
            data = self.to_dict(model)
            response = self.client.table(self.table_name).insert(data).execute()
            if response.data: 
                return self.to_model(response.data[0])
            return None
        #Caso de errado
        except Exception as e:
            print(f"Erro ao criar registro: {e}")
            return None
  
  ### Read 
  def read(self, pk: str, value: T) -> Optional[T]:
    try:
      response = self.client.table(self.table_name).select('*').eq(pk,value).execute()
      if response.data and len(response.data) > 0:
        return self.to_model (response.data[0])
      return None
    except Exception as e:
      print(f"Erro ao buscar registro: {e}")
      return None
    
  # Read All
  def read_all(self) -> List[T]:
    try:
      response = self.client.table(self.table_name).select('*').execute()
      if response.data:
        return [self.to_model(item) for item in response.data]
      return []
    except Exception as e:
      print(f"Erro ao buscar todos os registros: {e}")
      return []
  
  # Update
  def update(self, pk: str, value: T, model: T) -> Optional[T]:
        try:
            data = self.to_dict(model)
            response = self._client.table(self._table_name).update(data).eq(pk, value).execute()
            if response.data:
                return self.to_model(response.data[0])
            return None
        except Exception as e:
            print(f'Erro ao atualizar registro: {e}')
            return None
  
  # Delete
  def delete(self, pk: str, value: T) -> bool:
        try:
            response = self.client.table(self.table_name).delete().eq(pk, value).execute()
            return response.status_code == 200
        except Exception as e:
            print(f'Erro ao deletar registro: {e}')
            return False