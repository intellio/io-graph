from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedScopeSensitivityLabels(BaseModel):
	labelKind: Optional[LabelKind | str] = Field(alias="labelKind", default=None,)
	odata_type: Literal["#microsoft.graph.enumeratedScopeSensitivityLabels"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedScopeSensitivityLabels")
	sensitivityLabels: Optional[list[str]] = Field(alias="sensitivityLabels", default=None,)

from .label_kind import LabelKind

