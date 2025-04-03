from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LinkedResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.linkedResource"] = Field(alias="@odata.type", default="#microsoft.graph.linkedResource")
	applicationName: Optional[str] = Field(alias="applicationName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

