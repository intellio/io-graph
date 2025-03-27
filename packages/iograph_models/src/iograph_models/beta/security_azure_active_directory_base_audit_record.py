from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAzureActiveDirectoryBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.azureActiveDirectoryBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.azureActiveDirectoryBaseAuditRecord")


