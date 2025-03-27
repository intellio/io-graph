from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthAttestationState(BaseModel):
	attestationIdentityKey: Optional[str] = Field(alias="attestationIdentityKey", default=None,)
	bitLockerStatus: Optional[str] = Field(alias="bitLockerStatus", default=None,)
	bootAppSecurityVersion: Optional[str] = Field(alias="bootAppSecurityVersion", default=None,)
	bootDebugging: Optional[str] = Field(alias="bootDebugging", default=None,)
	bootManagerSecurityVersion: Optional[str] = Field(alias="bootManagerSecurityVersion", default=None,)
	bootManagerVersion: Optional[str] = Field(alias="bootManagerVersion", default=None,)
	bootRevisionListInfo: Optional[str] = Field(alias="bootRevisionListInfo", default=None,)
	codeIntegrity: Optional[str] = Field(alias="codeIntegrity", default=None,)
	codeIntegrityCheckVersion: Optional[str] = Field(alias="codeIntegrityCheckVersion", default=None,)
	codeIntegrityPolicy: Optional[str] = Field(alias="codeIntegrityPolicy", default=None,)
	contentNamespaceUrl: Optional[str] = Field(alias="contentNamespaceUrl", default=None,)
	contentVersion: Optional[str] = Field(alias="contentVersion", default=None,)
	dataExcutionPolicy: Optional[str] = Field(alias="dataExcutionPolicy", default=None,)
	deviceHealthAttestationStatus: Optional[str] = Field(alias="deviceHealthAttestationStatus", default=None,)
	earlyLaunchAntiMalwareDriverProtection: Optional[str] = Field(alias="earlyLaunchAntiMalwareDriverProtection", default=None,)
	healthAttestationSupportedStatus: Optional[str] = Field(alias="healthAttestationSupportedStatus", default=None,)
	healthStatusMismatchInfo: Optional[str] = Field(alias="healthStatusMismatchInfo", default=None,)
	issuedDateTime: Optional[datetime] = Field(alias="issuedDateTime", default=None,)
	lastUpdateDateTime: Optional[str] = Field(alias="lastUpdateDateTime", default=None,)
	operatingSystemKernelDebugging: Optional[str] = Field(alias="operatingSystemKernelDebugging", default=None,)
	operatingSystemRevListInfo: Optional[str] = Field(alias="operatingSystemRevListInfo", default=None,)
	pcr0: Optional[str] = Field(alias="pcr0", default=None,)
	pcrHashAlgorithm: Optional[str] = Field(alias="pcrHashAlgorithm", default=None,)
	resetCount: Optional[int] = Field(alias="resetCount", default=None,)
	restartCount: Optional[int] = Field(alias="restartCount", default=None,)
	safeMode: Optional[str] = Field(alias="safeMode", default=None,)
	secureBoot: Optional[str] = Field(alias="secureBoot", default=None,)
	secureBootConfigurationPolicyFingerPrint: Optional[str] = Field(alias="secureBootConfigurationPolicyFingerPrint", default=None,)
	testSigning: Optional[str] = Field(alias="testSigning", default=None,)
	tpmVersion: Optional[str] = Field(alias="tpmVersion", default=None,)
	virtualSecureMode: Optional[str] = Field(alias="virtualSecureMode", default=None,)
	windowsPE: Optional[str] = Field(alias="windowsPE", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


