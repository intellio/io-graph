from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPowerPlatformAdministratorActivityRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPlatformAdministratorActivityRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPlatformAdministratorActivityRecord")


