from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAuditCoreRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.auditCoreRoot"] = Field(alias="@odata.type",)
	queries: Optional[list[SecurityAuditLogQuery]] = Field(alias="queries", default=None,)

from .security_audit_log_query import SecurityAuditLogQuery
