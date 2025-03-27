from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HardwarePasswordInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	currentPassword: Optional[str] = Field(alias="currentPassword", default=None,)
	previousPasswords: Optional[list[str]] = Field(alias="previousPasswords", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)


