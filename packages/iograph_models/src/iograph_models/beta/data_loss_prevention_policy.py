from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DataLossPreventionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dataLossPreventionPolicy"] = Field(alias="@odata.type",)
	name: Optional[str] = Field(alias="name", default=None,)

