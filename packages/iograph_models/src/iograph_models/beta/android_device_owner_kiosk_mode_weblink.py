from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerKioskModeWeblink(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	link: Optional[str] = Field(alias="link",default=None,)


