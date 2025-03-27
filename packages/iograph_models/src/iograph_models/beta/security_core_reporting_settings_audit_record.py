from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCoreReportingSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.coreReportingSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.coreReportingSettingsAuditRecord")


