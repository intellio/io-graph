from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCdpResourceScopeChangeEventRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpResourceScopeChangeEventRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpResourceScopeChangeEventRecord")


