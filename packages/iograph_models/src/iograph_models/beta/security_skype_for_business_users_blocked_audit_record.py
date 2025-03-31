from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySkypeForBusinessUsersBlockedAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.skypeForBusinessUsersBlockedAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.skypeForBusinessUsersBlockedAuditRecord")

