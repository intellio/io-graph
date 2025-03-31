from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedAppStatusRaw(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedAppStatusRaw"] = Field(alias="@odata.type", default="#microsoft.graph.managedAppStatusRaw")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)

