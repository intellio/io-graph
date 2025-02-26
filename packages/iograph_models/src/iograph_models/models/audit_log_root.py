from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditLogRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	directoryAudits: list[DirectoryAudit] = Field(alias="directoryAudits",)
	provisioning: list[ProvisioningObjectSummary] = Field(alias="provisioning",)
	signIns: list[SignIn] = Field(alias="signIns",)

from .directory_audit import DirectoryAudit
from .provisioning_object_summary import ProvisioningObjectSummary
from .sign_in import SignIn

