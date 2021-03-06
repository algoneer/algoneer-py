from .result import Result, ResultProxy
from algoneer.algorithm import Algorithm
from algoneer.model import Model
from algoneer.object import Object

from typing import Dict, Any


class AlgorithmResult(Object, ResultProxy):
    def __init__(self, algorithm: Algorithm, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._algorithm = algorithm

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
