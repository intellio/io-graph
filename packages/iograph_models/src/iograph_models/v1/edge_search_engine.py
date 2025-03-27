from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EdgeSearchEngine(BaseModel):
	odata_type: Literal["#microsoft.graph.edgeSearchEngine"] = Field(alias="@odata.type", default="#microsoft.graph.edgeSearchEngine")
	edgeSearchEngineType: Optional[EdgeSearchEngineType | str] = Field(alias="edgeSearchEngineType", default=None,)

from .edge_search_engine_type import EdgeSearchEngineType

