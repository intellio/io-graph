from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NoDeviceRegistrationMembership(BaseModel):
	odata_type: Literal["#microsoft.graph.noDeviceRegistrationMembership"] = Field(alias="@odata.type", default="#microsoft.graph.noDeviceRegistrationMembership")


