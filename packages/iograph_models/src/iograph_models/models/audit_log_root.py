from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuditLogRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	directoryAudits: Optional[list[DirectoryAudit]] = Field(default=None,alias="directoryAudits",)
	provisioning: Optional[list[ProvisioningObjectSummary]] = Field(default=None,alias="provisioning",)
	signIns: Optional[list[SignIn]] = Field(default=None,alias="signIns",)

from .directory_audit import DirectoryAudit
from .provisioning_object_summary import ProvisioningObjectSummary
from .sign_in import SignIn

