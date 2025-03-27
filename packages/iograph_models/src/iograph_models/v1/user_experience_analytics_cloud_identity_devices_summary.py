from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsCloudIdentityDevicesSummary(BaseModel):
	deviceWithoutCloudIdentityCount: Optional[int] = Field(alias="deviceWithoutCloudIdentityCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


