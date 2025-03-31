from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AndroidDeviceOwnerKioskModeWeblink(BaseModel):
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerKioskModeWeblink"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerKioskModeWeblink")
	label: Optional[str] = Field(alias="label", default=None,)
	link: Optional[str] = Field(alias="link", default=None,)

