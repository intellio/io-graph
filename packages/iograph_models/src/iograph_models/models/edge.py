from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Edge(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	internetExplorerMode: Optional[InternetExplorerMode] = Field(default=None,alias="internetExplorerMode",)

from .internet_explorer_mode import InternetExplorerMode

