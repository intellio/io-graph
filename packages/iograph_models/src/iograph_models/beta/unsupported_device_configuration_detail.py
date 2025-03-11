from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnsupportedDeviceConfigurationDetail(BaseModel):
	message: Optional[str] = Field(alias="message",default=None,)
	propertyName: Optional[str] = Field(alias="propertyName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


