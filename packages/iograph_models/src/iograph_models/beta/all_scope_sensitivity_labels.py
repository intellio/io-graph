from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AllScopeSensitivityLabels(BaseModel):
	labelKind: Optional[LabelKind | str] = Field(alias="labelKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .label_kind import LabelKind

