from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Edge(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.edge"] = Field(alias="@odata.type",)
	internetExplorerMode: Optional[InternetExplorerMode] = Field(alias="internetExplorerMode", default=None,)

from .internet_explorer_mode import InternetExplorerMode
