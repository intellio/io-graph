from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceWindowsOperatingSystemUpdate(BaseModel):
	buildVersion: Optional[str] = Field(alias="buildVersion",default=None,)
	releaseMonth: Optional[int] = Field(alias="releaseMonth",default=None,)
	releaseYear: Optional[int] = Field(alias="releaseYear",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


