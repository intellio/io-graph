from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AndroidDeviceOwnerKioskModeApp(BaseModel):
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerKioskModeApp"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerKioskModeApp")
	className: Optional[str] = Field(alias="className", default=None,)
	package: Optional[str] = Field(alias="package", default=None,)

