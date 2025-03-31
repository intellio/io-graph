from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditLogRoot(BaseModel):
	customSecurityAttributeAudits: Optional[list[CustomSecurityAttributeAudit]] = Field(alias="customSecurityAttributeAudits", default=None,)
	directoryAudits: Optional[list[DirectoryAudit]] = Field(alias="directoryAudits", default=None,)
	directoryProvisioning: Optional[list[ProvisioningObjectSummary]] = Field(alias="directoryProvisioning", default=None,)
	provisioning: Optional[list[ProvisioningObjectSummary]] = Field(alias="provisioning", default=None,)
	signIns: Optional[list[SignIn]] = Field(alias="signIns", default=None,)
	signUps: Optional[list[SelfServiceSignUp]] = Field(alias="signUps", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .custom_security_attribute_audit import CustomSecurityAttributeAudit
from .directory_audit import DirectoryAudit
from .provisioning_object_summary import ProvisioningObjectSummary
from .sign_in import SignIn
from .self_service_sign_up import SelfServiceSignUp
