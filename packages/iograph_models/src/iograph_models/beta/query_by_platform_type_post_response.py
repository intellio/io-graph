from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Query_by_platform_typePostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[DeviceManagementResourceAccessProfileBase]]] = Field(alias="value",default=None,)

from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

