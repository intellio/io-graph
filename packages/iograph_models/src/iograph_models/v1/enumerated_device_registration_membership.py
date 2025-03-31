from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EnumeratedDeviceRegistrationMembership(BaseModel):
	odata_type: Literal["#microsoft.graph.enumeratedDeviceRegistrationMembership"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedDeviceRegistrationMembership")
	groups: Optional[list[str]] = Field(alias="groups", default=None,)
	users: Optional[list[str]] = Field(alias="users", default=None,)

