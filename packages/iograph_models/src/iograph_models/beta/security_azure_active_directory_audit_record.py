from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAzureActiveDirectoryAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.azureActiveDirectoryAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.azureActiveDirectoryAuditRecord")


