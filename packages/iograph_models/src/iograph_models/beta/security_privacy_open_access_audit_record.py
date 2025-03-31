from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPrivacyOpenAccessAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyOpenAccessAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyOpenAccessAuditRecord")

