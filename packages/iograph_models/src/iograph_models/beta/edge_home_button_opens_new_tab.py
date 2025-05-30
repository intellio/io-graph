from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class EdgeHomeButtonOpensNewTab(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeHomeButtonOpensNewTab"] = Field(alias="@odata.type", default="#microsoft.graph.edgeHomeButtonOpensNewTab")

