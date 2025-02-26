from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcSourceDeviceImage(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	subscriptionDisplayName: Optional[str] = Field(default=None,alias="subscriptionDisplayName",)
	subscriptionId: Optional[str] = Field(default=None,alias="subscriptionId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


