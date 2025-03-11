from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementBooleanSettingInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	definitionId: Optional[str] = Field(alias="definitionId",default=None,)
	valueJson: Optional[str] = Field(alias="valueJson",default=None,)
	value: Optional[bool] = Field(alias="value",default=None,)


