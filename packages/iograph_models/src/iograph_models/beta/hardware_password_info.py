from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class HardwarePasswordInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwarePasswordInfo"] = Field(alias="@odata.type", default="#microsoft.graph.hardwarePasswordInfo")
	currentPassword: Optional[str] = Field(alias="currentPassword", default=None,)
	previousPasswords: Optional[list[str]] = Field(alias="previousPasswords", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)

