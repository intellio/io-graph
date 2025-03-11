from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedDeviceRegistrationMembership(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groups: Optional[list[str]] = Field(alias="groups",default=None,)
	users: Optional[list[str]] = Field(alias="users",default=None,)


