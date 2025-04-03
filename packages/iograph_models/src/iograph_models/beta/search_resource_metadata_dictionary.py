from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SearchResourceMetadataDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.searchResourceMetadataDictionary"] = Field(alias="@odata.type", default="#microsoft.graph.searchResourceMetadataDictionary")

