from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityIoTDeviceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	devicePageLink: Optional[str] = Field(default=None,alias="devicePageLink",)
	deviceSubType: Optional[str] = Field(default=None,alias="deviceSubType",)
	deviceType: Optional[str] = Field(default=None,alias="deviceType",)
	importance: Optional[SecurityIoTDeviceImportanceType] = Field(default=None,alias="importance",)
	ioTHub: Optional[SecurityAzureResourceEvidence] = Field(default=None,alias="ioTHub",)
	ioTSecurityAgentId: Optional[str] = Field(default=None,alias="ioTSecurityAgentId",)
	ipAddress: Optional[SecurityIpEvidence] = Field(default=None,alias="ipAddress",)
	isAuthorized: Optional[bool] = Field(default=None,alias="isAuthorized",)
	isProgramming: Optional[bool] = Field(default=None,alias="isProgramming",)
	isScanner: Optional[bool] = Field(default=None,alias="isScanner",)
	macAddress: Optional[str] = Field(default=None,alias="macAddress",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	nics: Optional[list[SecurityNicEvidence]] = Field(default=None,alias="nics",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	owners: Optional[list[str]] = Field(default=None,alias="owners",)
	protocols: Optional[list[str]] = Field(default=None,alias="protocols",)
	purdueLayer: Optional[str] = Field(default=None,alias="purdueLayer",)
	sensor: Optional[str] = Field(default=None,alias="sensor",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	site: Optional[str] = Field(default=None,alias="site",)
	source: Optional[str] = Field(default=None,alias="source",)
	sourceRef: Optional[SecurityUrlEvidence] = Field(default=None,alias="sourceRef",)
	zone: Optional[str] = Field(default=None,alias="zone",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_io_t_device_importance_type import SecurityIoTDeviceImportanceType
from .security_azure_resource_evidence import SecurityAzureResourceEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_nic_evidence import SecurityNicEvidence
from .security_url_evidence import SecurityUrlEvidence

