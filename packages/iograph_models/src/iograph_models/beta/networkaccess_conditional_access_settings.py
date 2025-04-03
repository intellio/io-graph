from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.conditionalAccessSettings"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.conditionalAccessSettings")
	signalingStatus: Optional[NetworkaccessStatus | str] = Field(alias="signalingStatus", default=None,)

from .networkaccess_status import NetworkaccessStatus
