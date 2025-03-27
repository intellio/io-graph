from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAzureActiveDirectoryAccountLogonAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.azureActiveDirectoryAccountLogonAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.azureActiveDirectoryAccountLogonAuditRecord")


