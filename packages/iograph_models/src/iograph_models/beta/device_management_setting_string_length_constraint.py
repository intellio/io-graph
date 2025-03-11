from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingStringLengthConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumLength: Optional[int] = Field(alias="maximumLength",default=None,)
	minimumLength: Optional[int] = Field(alias="minimumLength",default=None,)


