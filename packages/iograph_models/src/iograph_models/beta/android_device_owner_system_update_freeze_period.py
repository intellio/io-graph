from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerSystemUpdateFreezePeriod(BaseModel):
	endDay: Optional[int] = Field(alias="endDay", default=None,)
	endMonth: Optional[int] = Field(alias="endMonth", default=None,)
	startDay: Optional[int] = Field(alias="startDay", default=None,)
	startMonth: Optional[int] = Field(alias="startMonth", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


