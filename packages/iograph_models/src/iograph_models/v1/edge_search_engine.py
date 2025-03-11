from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdgeSearchEngine(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	edgeSearchEngineType: Optional[EdgeSearchEngineType | str] = Field(alias="edgeSearchEngineType",default=None,)

from .edge_search_engine_type import EdgeSearchEngineType

