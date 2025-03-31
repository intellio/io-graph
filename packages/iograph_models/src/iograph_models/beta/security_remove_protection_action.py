from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityRemoveProtectionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.removeProtectionAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.removeProtectionAction")

