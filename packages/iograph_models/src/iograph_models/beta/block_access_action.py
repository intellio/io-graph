from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class BlockAccessAction(BaseModel):
	odata_type: Literal["#microsoft.graph.blockAccessAction"] = Field(alias="@odata.type", default="#microsoft.graph.blockAccessAction")

