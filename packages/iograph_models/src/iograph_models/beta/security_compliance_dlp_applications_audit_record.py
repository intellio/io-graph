from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpApplicationsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpApplicationsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpApplicationsAuditRecord")


