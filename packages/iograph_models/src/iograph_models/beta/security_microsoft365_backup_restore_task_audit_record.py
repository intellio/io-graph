from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoft365BackupRestoreTaskAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoft365BackupRestoreTaskAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoft365BackupRestoreTaskAuditRecord")

