from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class EdgeHomeButtonHidden(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeHomeButtonHidden"] = Field(alias="@odata.type", default="#microsoft.graph.edgeHomeButtonHidden")

