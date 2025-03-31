from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class EdgeHomeButtonLoadsStartPage(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeHomeButtonLoadsStartPage"] = Field(alias="@odata.type", default="#microsoft.graph.edgeHomeButtonLoadsStartPage")

