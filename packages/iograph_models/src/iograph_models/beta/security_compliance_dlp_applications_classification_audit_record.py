from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpApplicationsClassificationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpApplicationsClassificationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpApplicationsClassificationAuditRecord")


