from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SharedEmailDomain(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharedEmailDomain"] = Field(alias="@odata.type",)
	provisioningStatus: Optional[str] = Field(alias="provisioningStatus", default=None,)

