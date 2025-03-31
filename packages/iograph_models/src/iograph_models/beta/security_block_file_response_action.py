from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityBlockFileResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.blockFileResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.blockFileResponseAction")
	deviceGroupNames: Optional[list[str]] = Field(alias="deviceGroupNames", default=None,)
	identifier: Optional[SecurityFileEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_file_entity_identifier import SecurityFileEntityIdentifier
