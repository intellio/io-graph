from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcSourceDeviceImage(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	subscriptionDisplayName: Optional[str] = Field(alias="subscriptionDisplayName", default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

