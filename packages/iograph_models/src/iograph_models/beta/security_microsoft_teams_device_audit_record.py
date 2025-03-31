from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftTeamsDeviceAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsDeviceAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsDeviceAuditRecord")

