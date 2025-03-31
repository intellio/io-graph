from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoft365BackupBackupPolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoft365BackupBackupPolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoft365BackupBackupPolicyAuditRecord")

