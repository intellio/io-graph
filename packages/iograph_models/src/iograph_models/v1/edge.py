from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Edge(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	internetExplorerMode: Optional[InternetExplorerMode] = Field(alias="internetExplorerMode",default=None,)

from .internet_explorer_mode import InternetExplorerMode

