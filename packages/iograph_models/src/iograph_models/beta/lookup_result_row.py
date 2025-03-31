from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LookupResultRow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.lookupResultRow"] = Field(alias="@odata.type",)
	row: Optional[str] = Field(alias="row", default=None,)

