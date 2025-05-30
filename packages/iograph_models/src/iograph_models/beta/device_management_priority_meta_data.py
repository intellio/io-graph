from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementPriorityMetaData(BaseModel):
	priority: Optional[int] = Field(alias="priority", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

