from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10XSCEPCertificateProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10XSCEPCertificateProfile"] = Field(alias="@odata.type", default="#microsoft.graph.windows10XSCEPCertificateProfile")
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceManagementResourceAccessProfileAssignment]] = Field(alias="assignments", default=None,)
	certificateStore: Optional[CertificateStore | str] = Field(alias="certificateStore", default=None,)
	certificateValidityPeriodScale: Optional[CertificateValidityPeriodScale | str] = Field(alias="certificateValidityPeriodScale", default=None,)
	certificateValidityPeriodValue: Optional[int] = Field(alias="certificateValidityPeriodValue", default=None,)
	extendedKeyUsages: Optional[list[ExtendedKeyUsage]] = Field(alias="extendedKeyUsages", default=None,)
	hashAlgorithm: Optional[list[HashAlgorithms | str]] = Field(alias="hashAlgorithm", default=None,)
	keySize: Optional[KeySize | str] = Field(alias="keySize", default=None,)
	keyStorageProvider: Optional[KeyStorageProviderOption | str] = Field(alias="keyStorageProvider", default=None,)
	keyUsage: Optional[KeyUsages | str] = Field(alias="keyUsage", default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage", default=None,)
	rootCertificateId: Optional[UUID] = Field(alias="rootCertificateId", default=None,)
	scepServerUrls: Optional[list[str]] = Field(alias="scepServerUrls", default=None,)
	subjectAlternativeNameFormats: Optional[list[Windows10XCustomSubjectAlternativeName]] = Field(alias="subjectAlternativeNameFormats", default=None,)
	subjectNameFormatString: Optional[str] = Field(alias="subjectNameFormatString", default=None,)

from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
from .certificate_store import CertificateStore
from .certificate_validity_period_scale import CertificateValidityPeriodScale
from .extended_key_usage import ExtendedKeyUsage
from .hash_algorithms import HashAlgorithms
from .key_size import KeySize
from .key_storage_provider_option import KeyStorageProviderOption
from .key_usages import KeyUsages
from .windows10_x_custom_subject_alternative_name import Windows10XCustomSubjectAlternativeName
