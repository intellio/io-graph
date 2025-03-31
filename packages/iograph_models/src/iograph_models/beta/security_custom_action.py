from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCustomAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.customAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.customAction")
	name: Optional[str] = Field(alias="name", default=None,)
	properties: Optional[list[SecurityKeyValuePair]] = Field(alias="properties", default=None,)

from .security_key_value_pair import SecurityKeyValuePair
