from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EdgeSearchEngine(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	edgeSearchEngineType: Optional[EdgeSearchEngineType] = Field(default=None,alias="edgeSearchEngineType",)

from .edge_search_engine_type import EdgeSearchEngineType

