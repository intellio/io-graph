from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityOwaGetAccessTokenForResourceAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.owaGetAccessTokenForResourceAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.owaGetAccessTokenForResourceAuditRecord")


