from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIoTDeviceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	devicePageLink: Optional[str] = Field(alias="devicePageLink",default=None,)
	deviceSubType: Optional[str] = Field(alias="deviceSubType",default=None,)
	deviceType: Optional[str] = Field(alias="deviceType",default=None,)
	importance: Optional[SecurityIoTDeviceImportanceType | str] = Field(alias="importance",default=None,)
	ioTHub: Optional[SecurityAzureResourceEvidence] = Field(alias="ioTHub",default=None,)
	ioTSecurityAgentId: Optional[str] = Field(alias="ioTSecurityAgentId",default=None,)
	ipAddress: Optional[SecurityIpEvidence] = Field(alias="ipAddress",default=None,)
	isAuthorized: Optional[bool] = Field(alias="isAuthorized",default=None,)
	isProgramming: Optional[bool] = Field(alias="isProgramming",default=None,)
	isScanner: Optional[bool] = Field(alias="isScanner",default=None,)
	macAddress: Optional[str] = Field(alias="macAddress",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	nics: Optional[list[SecurityNicEvidence]] = Field(alias="nics",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	owners: Optional[list[str]] = Field(alias="owners",default=None,)
	protocols: Optional[list[str]] = Field(alias="protocols",default=None,)
	purdueLayer: Optional[str] = Field(alias="purdueLayer",default=None,)
	sensor: Optional[str] = Field(alias="sensor",default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber",default=None,)
	site: Optional[str] = Field(alias="site",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)
	sourceRef: Optional[SecurityUrlEvidence] = Field(alias="sourceRef",default=None,)
	zone: Optional[str] = Field(alias="zone",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_io_t_device_importance_type import SecurityIoTDeviceImportanceType
from .security_azure_resource_evidence import SecurityAzureResourceEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_nic_evidence import SecurityNicEvidence
from .security_url_evidence import SecurityUrlEvidence

