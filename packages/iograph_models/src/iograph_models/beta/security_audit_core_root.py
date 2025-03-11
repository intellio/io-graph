from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAuditCoreRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	queries: Optional[list[SecurityAuditLogQuery]] = Field(alias="queries",default=None,)

from .security_audit_log_query import SecurityAuditLogQuery

