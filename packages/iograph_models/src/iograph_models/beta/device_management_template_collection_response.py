from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[DeviceManagementTemplate]]] = Field(alias="value",default=None,)

from .device_management_template import DeviceManagementTemplate

