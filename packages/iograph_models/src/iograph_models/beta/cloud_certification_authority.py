from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudCertificationAuthority(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificateDownloadUrl: Optional[str] = Field(alias="certificateDownloadUrl",default=None,)
	certificateKeySize: Optional[CloudCertificationAuthorityCertificateKeySize | str] = Field(alias="certificateKeySize",default=None,)
	certificateRevocationListUrl: Optional[str] = Field(alias="certificateRevocationListUrl",default=None,)
	certificateSigningRequest: Optional[str] = Field(alias="certificateSigningRequest",default=None,)
	certificationAuthorityIssuerId: Optional[str] = Field(alias="certificationAuthorityIssuerId",default=None,)
	certificationAuthorityIssuerUri: Optional[str] = Field(alias="certificationAuthorityIssuerUri",default=None,)
	certificationAuthorityStatus: Optional[CloudCertificationAuthorityStatus | str] = Field(alias="certificationAuthorityStatus",default=None,)
	cloudCertificationAuthorityHashingAlgorithm: Optional[CloudCertificationAuthorityHashingAlgorithm | str] = Field(alias="cloudCertificationAuthorityHashingAlgorithm",default=None,)
	cloudCertificationAuthorityType: Optional[CloudCertificationAuthorityType | str] = Field(alias="cloudCertificationAuthorityType",default=None,)
	commonName: Optional[str] = Field(alias="commonName",default=None,)
	countryName: Optional[str] = Field(alias="countryName",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	eTag: Optional[str] = Field(alias="eTag",default=None,)
	extendedKeyUsages: Optional[list[ExtendedKeyUsage]] = Field(alias="extendedKeyUsages",default=None,)
	issuerCommonName: Optional[str] = Field(alias="issuerCommonName",default=None,)
	keyPlatform: Optional[CloudCertificationAuthorityKeyPlatformType | str] = Field(alias="keyPlatform",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	localityName: Optional[str] = Field(alias="localityName",default=None,)
	ocspResponderUri: Optional[str] = Field(alias="ocspResponderUri",default=None,)
	organizationName: Optional[str] = Field(alias="organizationName",default=None,)
	organizationUnit: Optional[str] = Field(alias="organizationUnit",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	rootCertificateCommonName: Optional[str] = Field(alias="rootCertificateCommonName",default=None,)
	scepServerUrl: Optional[str] = Field(alias="scepServerUrl",default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber",default=None,)
	stateName: Optional[str] = Field(alias="stateName",default=None,)
	subjectName: Optional[str] = Field(alias="subjectName",default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint",default=None,)
	validityEndDateTime: Optional[datetime] = Field(alias="validityEndDateTime",default=None,)
	validityPeriodInYears: Optional[int] = Field(alias="validityPeriodInYears",default=None,)
	validityStartDateTime: Optional[datetime] = Field(alias="validityStartDateTime",default=None,)
	versionNumber: Optional[int] = Field(alias="versionNumber",default=None,)
	cloudCertificationAuthorityLeafCertificate: Optional[list[CloudCertificationAuthorityLeafCertificate]] = Field(alias="cloudCertificationAuthorityLeafCertificate",default=None,)

from .cloud_certification_authority_certificate_key_size import CloudCertificationAuthorityCertificateKeySize
from .cloud_certification_authority_status import CloudCertificationAuthorityStatus
from .cloud_certification_authority_hashing_algorithm import CloudCertificationAuthorityHashingAlgorithm
from .cloud_certification_authority_type import CloudCertificationAuthorityType
from .extended_key_usage import ExtendedKeyUsage
from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate

