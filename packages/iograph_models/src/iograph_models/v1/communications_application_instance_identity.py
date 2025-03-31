from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CommunicationsApplicationInstanceIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.communicationsApplicationInstanceIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.communicationsApplicationInstanceIdentity")
	hidden: Optional[bool] = Field(alias="hidden", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

