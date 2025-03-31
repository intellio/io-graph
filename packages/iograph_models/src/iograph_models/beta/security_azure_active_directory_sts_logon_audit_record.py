from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAzureActiveDirectoryStsLogonAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.azureActiveDirectoryStsLogonAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.azureActiveDirectoryStsLogonAuditRecord")

