from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuditLogRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.auditLogRoot"] = Field(alias="@odata.type",)
	directoryAudits: Optional[list[DirectoryAudit]] = Field(alias="directoryAudits", default=None,)
	provisioning: Optional[list[ProvisioningObjectSummary]] = Field(alias="provisioning", default=None,)
	signIns: Optional[list[SignIn]] = Field(alias="signIns", default=None,)

from .directory_audit import DirectoryAudit
from .provisioning_object_summary import ProvisioningObjectSummary
from .sign_in import SignIn
