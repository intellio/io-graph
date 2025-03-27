from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProtectDoNotForwardAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.protectDoNotForwardAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.protectDoNotForwardAction")


