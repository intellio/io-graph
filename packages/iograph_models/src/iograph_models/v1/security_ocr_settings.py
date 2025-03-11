from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityOcrSettings(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	maxImageSize: Optional[int] = Field(alias="maxImageSize",default=None,)
	timeout: Optional[str] = Field(alias="timeout",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


