import abc

import algoneer.model
from algoneer.project import Project
from algoneer.object import Object
from algoneer.dataset import Dataset
from algoneer.algorithmschema import AlgorithmSchema

from typing import Optional, Dict, Any


class Algorithm(Object):
    def __init__(self, project: Project, schema: AlgorithmSchema) -> None:
        super().__init__()
        self._schema = schema
        self._algorithmschema = AlgorithmAlgorithmSchema(self, self.schema)
        self._project = project

    def __getattr__(self, attr):
        if attr.startswith("is_"):
            _type = attr[3:]
            if self.schema is not None and self.schema.type.name.lower() == _type:
                return True
            return False
        return super().__getattr__(attr)

    def load(self, data: Dict[str, Any]) -> None:
        pass

    def dump(self) -> Dict[str, Any]:
        return {"data": self.data, "name": self.name}

    @property
    def project(self):
        return self._project

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def data(self) -> Dict[str, Any]:
        pass

    @property
    def schema(self) -> AlgorithmSchema:
        return self._schema

    @schema.setter
    def schema(self, schema: AlgorithmSchema) -> None:
        self.schema = schema

    @property
    def algorithm_schema(self) -> "AlgorithmAlgorithmSchema":
        return self._algorithmschema

    @abc.abstractmethod
    def fit(self, data: Dataset) -> "algoneer.model.Model":
        pass


class AlgorithmAlgorithmSchema(Object):
    def __init__(self, algorithm: Algorithm, schema: AlgorithmSchema):
        self.algorithm = algorithm
        self.schema = schema

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
