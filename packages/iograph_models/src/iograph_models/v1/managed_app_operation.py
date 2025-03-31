from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedAppOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedAppOperation"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

