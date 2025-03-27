from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementUserRightsLocalUserOrGroup(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	securityIdentifier: Optional[str] = Field(alias="securityIdentifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


