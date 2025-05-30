from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceWithoutCloudIdentityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = Field(alias="value", default=None,)

from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
