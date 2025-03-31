from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EdgeSearchEngineCustom(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeSearchEngineCustom"] = Field(alias="@odata.type", default="#microsoft.graph.edgeSearchEngineCustom")
	edgeSearchEngineOpenSearchXmlUrl: Optional[str] = Field(alias="edgeSearchEngineOpenSearchXmlUrl", default=None,)

