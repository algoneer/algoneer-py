from enum import Enum

from typing import Mapping, Iterable, Any

import algoneer.dataschema as dataschema
import algoneer.dataset as dataset


class AttributeSchema:
    class Type(Enum):

        Numerical = 1
        Timestamp = 2
        Integer = 3
        Float = 4
        Ordinal = 5
        Categorical = 6
        Unknown = 7

    def __init__(
        self,
        ds: "dataschema.DataSchema",
        column: str,
        type: Type,
        config: Mapping[str, Any],
    ) -> None:
        self._ds = ds
        self._type = type
        self._column = column
        self._config = config

    @property
    def config(self):
        return self._config

    @property
    def type(self):
        return self._type

    @property
    def column(self):
        return self._column

    def enforce(self, ds: "dataset.DataSet"):
        # we can test our luck...
        ds[self.column] = ds[self.column].astype(self._type, **self.config)
