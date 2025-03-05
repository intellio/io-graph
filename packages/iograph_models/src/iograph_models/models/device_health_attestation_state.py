from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthAttestationState(BaseModel):
	attestationIdentityKey: Optional[str] = Field(default=None,alias="attestationIdentityKey",)
	bitLockerStatus: Optional[str] = Field(default=None,alias="bitLockerStatus",)
	bootAppSecurityVersion: Optional[str] = Field(default=None,alias="bootAppSecurityVersion",)
	bootDebugging: Optional[str] = Field(default=None,alias="bootDebugging",)
	bootManagerSecurityVersion: Optional[str] = Field(default=None,alias="bootManagerSecurityVersion",)
	bootManagerVersion: Optional[str] = Field(default=None,alias="bootManagerVersion",)
	bootRevisionListInfo: Optional[str] = Field(default=None,alias="bootRevisionListInfo",)
	codeIntegrity: Optional[str] = Field(default=None,alias="codeIntegrity",)
	codeIntegrityCheckVersion: Optional[str] = Field(default=None,alias="codeIntegrityCheckVersion",)
	codeIntegrityPolicy: Optional[str] = Field(default=None,alias="codeIntegrityPolicy",)
	contentNamespaceUrl: Optional[str] = Field(default=None,alias="contentNamespaceUrl",)
	contentVersion: Optional[str] = Field(default=None,alias="contentVersion",)
	dataExcutionPolicy: Optional[str] = Field(default=None,alias="dataExcutionPolicy",)
	deviceHealthAttestationStatus: Optional[str] = Field(default=None,alias="deviceHealthAttestationStatus",)
	earlyLaunchAntiMalwareDriverProtection: Optional[str] = Field(default=None,alias="earlyLaunchAntiMalwareDriverProtection",)
	healthAttestationSupportedStatus: Optional[str] = Field(default=None,alias="healthAttestationSupportedStatus",)
	healthStatusMismatchInfo: Optional[str] = Field(default=None,alias="healthStatusMismatchInfo",)
	issuedDateTime: Optional[datetime] = Field(default=None,alias="issuedDateTime",)
	lastUpdateDateTime: Optional[str] = Field(default=None,alias="lastUpdateDateTime",)
	operatingSystemKernelDebugging: Optional[str] = Field(default=None,alias="operatingSystemKernelDebugging",)
	operatingSystemRevListInfo: Optional[str] = Field(default=None,alias="operatingSystemRevListInfo",)
	pcr0: Optional[str] = Field(default=None,alias="pcr0",)
	pcrHashAlgorithm: Optional[str] = Field(default=None,alias="pcrHashAlgorithm",)
	resetCount: Optional[int] = Field(default=None,alias="resetCount",)
	restartCount: Optional[int] = Field(default=None,alias="restartCount",)
	safeMode: Optional[str] = Field(default=None,alias="safeMode",)
	secureBoot: Optional[str] = Field(default=None,alias="secureBoot",)
	secureBootConfigurationPolicyFingerPrint: Optional[str] = Field(default=None,alias="secureBootConfigurationPolicyFingerPrint",)
	testSigning: Optional[str] = Field(default=None,alias="testSigning",)
	tpmVersion: Optional[str] = Field(default=None,alias="tpmVersion",)
	virtualSecureMode: Optional[str] = Field(default=None,alias="virtualSecureMode",)
	windowsPE: Optional[str] = Field(default=None,alias="windowsPE",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


