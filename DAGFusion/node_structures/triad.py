from __future__ import annotations
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
  from DAGFusion import TensorNode
  from DAGFusion.node_structures import Dyad

class Triad():
  def __init__(self, l_operand: TensorNode, r_operand: TensorNode, 
               outcome: TensorNode, operator: str) -> None:
    self.l = l_operand
    self.r = r_operand
    self.o = outcome
    self.operator = operator

  def set_next(self, next_adic: Triad|Dyad) -> None:
    self.next = next_adic
  
  def set_prev(self, prev_adics: Tuple[Triad|Dyad]) -> None:
    self.prev = prev_adics
  
  def get_operator(self) -> str:
    return self.operator
  
  def get_outcome(self) -> TensorNode:
    return self.o
  
  def __repr__(self) -> str:
    return f'Triad({self.l.name}, {self.r.name}, {self.o.name}; {self.operator})'