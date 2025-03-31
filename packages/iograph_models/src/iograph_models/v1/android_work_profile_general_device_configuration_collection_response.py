from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidWorkProfileGeneralDeviceConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidWorkProfileGeneralDeviceConfiguration]] = Field(alias="value", default=None,)

from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
