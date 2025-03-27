from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAipProtectionActionLogRequest(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aipProtectionActionLogRequest"] = Field(alias="@odata.type", default="#microsoft.graph.security.aipProtectionActionLogRequest")


