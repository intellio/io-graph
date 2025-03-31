from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AllScopeSensitivityLabels(BaseModel):
	labelKind: Optional[LabelKind | str] = Field(alias="labelKind", default=None,)
	odata_type: Literal["#microsoft.graph.allScopeSensitivityLabels"] = Field(alias="@odata.type", default="#microsoft.graph.allScopeSensitivityLabels")

from .label_kind import LabelKind
