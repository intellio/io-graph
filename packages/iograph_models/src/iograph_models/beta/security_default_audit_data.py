from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDefaultAuditData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.defaultAuditData"] = Field(alias="@odata.type", default="#microsoft.graph.security.defaultAuditData")


