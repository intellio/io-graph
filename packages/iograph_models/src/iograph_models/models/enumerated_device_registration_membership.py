from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnumeratedDeviceRegistrationMembership(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	groups: list[Optional[str]] = Field(alias="groups",)
	users: list[Optional[str]] = Field(alias="users",)


