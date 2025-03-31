from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessFqdn(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.fqdn"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.fqdn")
	value: Optional[str] = Field(alias="value", default=None,)

