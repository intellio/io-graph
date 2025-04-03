from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedDeviceCertificateState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceCertificateState"] = Field(alias="@odata.type", default="#microsoft.graph.managedDeviceCertificateState")
	certificateEnhancedKeyUsage: Optional[str] = Field(alias="certificateEnhancedKeyUsage", default=None,)
	certificateErrorCode: Optional[int] = Field(alias="certificateErrorCode", default=None,)
	certificateExpirationDateTime: Optional[datetime] = Field(alias="certificateExpirationDateTime", default=None,)
	certificateIssuanceDateTime: Optional[datetime] = Field(alias="certificateIssuanceDateTime", default=None,)
	certificateIssuanceState: Optional[CertificateIssuanceStates | str] = Field(alias="certificateIssuanceState", default=None,)
	certificateIssuer: Optional[str] = Field(alias="certificateIssuer", default=None,)
	certificateKeyLength: Optional[int] = Field(alias="certificateKeyLength", default=None,)
	certificateKeyStorageProvider: Optional[KeyStorageProviderOption | str] = Field(alias="certificateKeyStorageProvider", default=None,)
	certificateKeyUsage: Optional[KeyUsages | str] = Field(alias="certificateKeyUsage", default=None,)
	certificateLastIssuanceStateChangedDateTime: Optional[datetime] = Field(alias="certificateLastIssuanceStateChangedDateTime", default=None,)
	certificateProfileDisplayName: Optional[str] = Field(alias="certificateProfileDisplayName", default=None,)
	certificateRevokeStatus: Optional[CertificateRevocationStatus | str] = Field(alias="certificateRevokeStatus", default=None,)
	certificateSerialNumber: Optional[str] = Field(alias="certificateSerialNumber", default=None,)
	certificateSubjectAlternativeNameFormat: Optional[SubjectAlternativeNameType | str] = Field(alias="certificateSubjectAlternativeNameFormat", default=None,)
	certificateSubjectAlternativeNameFormatString: Optional[str] = Field(alias="certificateSubjectAlternativeNameFormatString", default=None,)
	certificateSubjectNameFormat: Optional[SubjectNameFormat | str] = Field(alias="certificateSubjectNameFormat", default=None,)
	certificateSubjectNameFormatString: Optional[str] = Field(alias="certificateSubjectNameFormatString", default=None,)
	certificateThumbprint: Optional[str] = Field(alias="certificateThumbprint", default=None,)
	certificateValidityPeriod: Optional[int] = Field(alias="certificateValidityPeriod", default=None,)
	certificateValidityPeriodUnits: Optional[CertificateValidityPeriodScale | str] = Field(alias="certificateValidityPeriodUnits", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	devicePlatform: Optional[DevicePlatformType | str] = Field(alias="devicePlatform", default=None,)
	lastCertificateStateChangeDateTime: Optional[datetime] = Field(alias="lastCertificateStateChangeDateTime", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)

from .certificate_issuance_states import CertificateIssuanceStates
from .key_storage_provider_option import KeyStorageProviderOption
from .key_usages import KeyUsages
from .certificate_revocation_status import CertificateRevocationStatus
from .subject_alternative_name_type import SubjectAlternativeNameType
from .subject_name_format import SubjectNameFormat
from .certificate_validity_period_scale import CertificateValidityPeriodScale
from .device_platform_type import DevicePlatformType
