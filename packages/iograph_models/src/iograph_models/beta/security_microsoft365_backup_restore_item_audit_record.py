from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoft365BackupRestoreItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoft365BackupRestoreItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoft365BackupRestoreItemAuditRecord")


