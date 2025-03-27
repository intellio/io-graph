from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AllDeviceRegistrationMembership(BaseModel):
	odata_type: Literal["#microsoft.graph.allDeviceRegistrationMembership"] = Field(alias="@odata.type", default="#microsoft.graph.allDeviceRegistrationMembership")


