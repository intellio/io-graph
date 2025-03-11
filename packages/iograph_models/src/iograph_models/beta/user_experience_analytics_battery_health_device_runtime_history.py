from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	estimatedRuntimeInMinutes: Optional[int] = Field(alias="estimatedRuntimeInMinutes",default=None,)
	runtimeDateTime: Optional[str] = Field(alias="runtimeDateTime",default=None,)


