from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChromeOSDeviceProperty(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	updatable: Optional[bool] = Field(alias="updatable",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	valueType: Optional[str] = Field(alias="valueType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


