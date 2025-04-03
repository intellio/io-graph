from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ColumnLink(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.columnLink"] = Field(alias="@odata.type", default="#microsoft.graph.columnLink")
	name: Optional[str] = Field(alias="name", default=None,)

