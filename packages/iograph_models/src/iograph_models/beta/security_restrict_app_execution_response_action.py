from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityRestrictAppExecutionResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.restrictAppExecutionResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.restrictAppExecutionResponseAction")
	identifier: Optional[SecurityDeviceIdEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_device_id_entity_identifier import SecurityDeviceIdEntityIdentifier
