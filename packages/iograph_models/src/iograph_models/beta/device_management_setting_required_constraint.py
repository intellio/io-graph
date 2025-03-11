from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingRequiredConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	notConfiguredValue: Optional[str] = Field(alias="notConfiguredValue",default=None,)


