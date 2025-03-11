from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceWithoutCloudIdentity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureAdDeviceId: Optional[str] = Field(alias="azureAdDeviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)


