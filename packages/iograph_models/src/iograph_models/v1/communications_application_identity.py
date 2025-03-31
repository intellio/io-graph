from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CommunicationsApplicationIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.communicationsApplicationIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.communicationsApplicationIdentity")
	applicationType: Optional[str] = Field(alias="applicationType", default=None,)
	hidden: Optional[bool] = Field(alias="hidden", default=None,)

