from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedDeviceRegistrationMembership(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	groups: Optional[list[str]] = Field(default=None,alias="groups",)
	users: Optional[list[str]] = Field(default=None,alias="users",)


