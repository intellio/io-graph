from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosDeviceType(BaseModel):
	iPad: Optional[bool] = Field(alias="iPad", default=None,)
	iPhoneAndIPod: Optional[bool] = Field(alias="iPhoneAndIPod", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


