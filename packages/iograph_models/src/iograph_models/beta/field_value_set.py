from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class FieldValueSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fieldValueSet"] = Field(alias="@odata.type",)

