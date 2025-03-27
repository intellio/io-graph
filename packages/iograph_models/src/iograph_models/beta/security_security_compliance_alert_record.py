from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySecurityComplianceAlertRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.securityComplianceAlertRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.securityComplianceAlertRecord")


