from dataclasses import dataclass, asdict
from typing import List, Optional
import json
import os
# -------------------- Modelo --------------------
@dataclass
class Servico:
    id: int
    nome: str
    descricao: str = ""
    preco: float = 0.0
    # getters e setters sendo feitos pelo dataclass; adiciono validação simples
    def set_preco(self, preco: float):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
    self.preco = float(preco)
    def to_dict(self) -> dict:
        return asdict(self)
    @staticmethod
    def from_dict(d: dict) -> 'Servico':
        return Servico(id=int(d['id']), nome=d['nome'], descricao=d.get('descricao',''),
    preco=float(d.get('preco',0.0)))
# -------------------- DAO --------------------
class ServicoDAO:
    def __init__(self, arquivo: str = 'servicos.json'):
        self.arquivo = arquivo
        self._servicos: List[Servico] = []
        self._load()
    def _load(self):
        if not os.path.exists(self.arquivo):
            self._servicos = []
        return
    try:
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self._servicos = [Servico.from_dict(item) for item in data]
    except Exception:
    # se o arquivo estiver corrompido, reinicializa
        self._servicos = []
    def _save(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([s.to_dict() for s in self._servicos], f, ensure_ascii=False, indent=2)

    def inserir(self, servico: Servico) -> None:
        if self.buscar_por_id(servico.id) is not None:
            raise ValueError(f"Serviço com id {servico.id} já existe")
            self._servicos.append(servico)
            self._save()
    def listar(self) -> List[Servico]:
        return list(self._servicos)
    def buscar_por_id(self, id: int) -> Optional[Servico]:
        for s in self._servicos:
            if s.id == id:
                return s
        return None
    def atualizar(self, servico: Servico) -> None:
        for idx, s in enumerate(self._servicos):
            if s.id == servico.id:
                self._servicos[idx] = servico
    view.mostrar()