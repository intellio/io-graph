from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcAutopilotConfiguration(BaseModel):
	applicationTimeoutInMinutes: Optional[int] = Field(alias="applicationTimeoutInMinutes", default=None,)
	devicePreparationProfileId: Optional[str] = Field(alias="devicePreparationProfileId", default=None,)
	onFailureDeviceAccessDenied: Optional[bool] = Field(alias="onFailureDeviceAccessDenied", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


