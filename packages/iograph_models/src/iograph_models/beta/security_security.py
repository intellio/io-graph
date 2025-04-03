from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySecurity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.security"] = Field(alias="@odata.type", default="#microsoft.graph.security.security")
	informationProtection: Optional[SecurityInformationProtection] = Field(alias="informationProtection", default=None,)

from .security_information_protection import SecurityInformationProtection
