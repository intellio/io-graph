from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDiscoveredCloudAppInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	csaStarLevel: Optional[SecurityAppInfoCsaStarLevel | str] = Field(alias="csaStarLevel", default=None,)
	dataAtRestEncryptionMethod: Optional[SecurityAppInfoDataAtRestEncryptionMethod | str] = Field(alias="dataAtRestEncryptionMethod", default=None,)
	dataCenter: Optional[str] = Field(alias="dataCenter", default=None,)
	dataRetentionPolicy: Optional[SecurityAppInfoDataRetentionPolicy | str] = Field(alias="dataRetentionPolicy", default=None,)
	dataTypes: Optional[SecurityAppInfoUploadedDataTypes | str] = Field(alias="dataTypes", default=None,)
	domainRegistrationDateTime: Optional[datetime] = Field(alias="domainRegistrationDateTime", default=None,)
	encryptionProtocol: Optional[SecurityAppInfoEncryptionProtocol | str] = Field(alias="encryptionProtocol", default=None,)
	fedRampLevel: Optional[SecurityAppInfoFedRampLevel | str] = Field(alias="fedRampLevel", default=None,)
	founded: Optional[int] = Field(alias="founded", default=None,)
	gdprReadinessStatement: Optional[str] = Field(alias="gdprReadinessStatement", default=None,)
	headquarters: Optional[str] = Field(alias="headquarters", default=None,)
	holding: Optional[SecurityAppInfoHolding | str] = Field(alias="holding", default=None,)
	hostingCompany: Optional[str] = Field(alias="hostingCompany", default=None,)
	isAdminAuditTrail: Optional[SecurityCloudAppInfoState | str] = Field(alias="isAdminAuditTrail", default=None,)
	isCobitCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isCobitCompliant", default=None,)
	isCoppaCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isCoppaCompliant", default=None,)
	isDataAuditTrail: Optional[SecurityCloudAppInfoState | str] = Field(alias="isDataAuditTrail", default=None,)
	isDataClassification: Optional[SecurityCloudAppInfoState | str] = Field(alias="isDataClassification", default=None,)
	isDataOwnership: Optional[SecurityCloudAppInfoState | str] = Field(alias="isDataOwnership", default=None,)
	isDisasterRecoveryPlan: Optional[SecurityCloudAppInfoState | str] = Field(alias="isDisasterRecoveryPlan", default=None,)
	isDmca: Optional[SecurityCloudAppInfoState | str] = Field(alias="isDmca", default=None,)
	isFerpaCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isFerpaCompliant", default=None,)
	isFfiecCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isFfiecCompliant", default=None,)
	isFileSharing: Optional[SecurityCloudAppInfoState | str] = Field(alias="isFileSharing", default=None,)
	isFinraCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isFinraCompliant", default=None,)
	isFismaCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isFismaCompliant", default=None,)
	isGaapCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGaapCompliant", default=None,)
	isGdprDataProtectionImpactAssessment: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprDataProtectionImpactAssessment", default=None,)
	isGdprDataProtectionOfficer: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprDataProtectionOfficer", default=None,)
	isGdprDataProtectionSecureCrossBorderDataTransfer: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprDataProtectionSecureCrossBorderDataTransfer", default=None,)
	isGdprImpactAssessment: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprImpactAssessment", default=None,)
	isGdprLawfulBasisForProcessing: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprLawfulBasisForProcessing", default=None,)
	isGdprReportDataBreaches: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprReportDataBreaches", default=None,)
	isGdprRightsRelatedToAutomatedDecisionMaking: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightsRelatedToAutomatedDecisionMaking", default=None,)
	isGdprRightToAccess: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToAccess", default=None,)
	isGdprRightToBeInformed: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToBeInformed", default=None,)
	isGdprRightToDataPortablility: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToDataPortablility", default=None,)
	isGdprRightToErasure: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToErasure", default=None,)
	isGdprRightToObject: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToObject", default=None,)
	isGdprRightToRectification: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToRectification", default=None,)
	isGdprRightToRestrictionOfProcessing: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprRightToRestrictionOfProcessing", default=None,)
	isGdprSecureCrossBorderDataControl: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGdprSecureCrossBorderDataControl", default=None,)
	isGlbaCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isGlbaCompliant", default=None,)
	isHipaaCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHipaaCompliant", default=None,)
	isHitrustCsfCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHitrustCsfCompliant", default=None,)
	isHttpSecurityHeadersContentSecurityPolicy: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHttpSecurityHeadersContentSecurityPolicy", default=None,)
	isHttpSecurityHeadersStrictTransportSecurity: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHttpSecurityHeadersStrictTransportSecurity", default=None,)
	isHttpSecurityHeadersXContentTypeOptions: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHttpSecurityHeadersXContentTypeOptions", default=None,)
	isHttpSecurityHeadersXFrameOptions: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHttpSecurityHeadersXFrameOptions", default=None,)
	isHttpSecurityHeadersXXssProtection: Optional[SecurityCloudAppInfoState | str] = Field(alias="isHttpSecurityHeadersXXssProtection", default=None,)
	isIpAddressRestriction: Optional[SecurityCloudAppInfoState | str] = Field(alias="isIpAddressRestriction", default=None,)
	isIsae3402Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isIsae3402Compliant", default=None,)
	isIso27001Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isIso27001Compliant", default=None,)
	isIso27017Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isIso27017Compliant", default=None,)
	isIso27018Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isIso27018Compliant", default=None,)
	isItarCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isItarCompliant", default=None,)
	isMultiFactorAuthentication: Optional[SecurityCloudAppInfoState | str] = Field(alias="isMultiFactorAuthentication", default=None,)
	isPasswordPolicy: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicy", default=None,)
	isPasswordPolicyChangePasswordPeriod: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicyChangePasswordPeriod", default=None,)
	isPasswordPolicyCharacterCombination: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicyCharacterCombination", default=None,)
	isPasswordPolicyPasswordHistoryAndReuse: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicyPasswordHistoryAndReuse", default=None,)
	isPasswordPolicyPasswordLengthLimit: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicyPasswordLengthLimit", default=None,)
	isPasswordPolicyPersonalInformationUse: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPasswordPolicyPersonalInformationUse", default=None,)
	isPenetrationTesting: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPenetrationTesting", default=None,)
	isPrivacyShieldCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isPrivacyShieldCompliant", default=None,)
	isRememberPassword: Optional[SecurityCloudAppInfoState | str] = Field(alias="isRememberPassword", default=None,)
	isRequiresUserAuthentication: Optional[SecurityCloudAppInfoState | str] = Field(alias="isRequiresUserAuthentication", default=None,)
	isSoc1Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSoc1Compliant", default=None,)
	isSoc2Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSoc2Compliant", default=None,)
	isSoc3Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSoc3Compliant", default=None,)
	isSoxCompliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSoxCompliant", default=None,)
	isSp80053Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSp80053Compliant", default=None,)
	isSsae16Compliant: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSsae16Compliant", default=None,)
	isSupportsSaml: Optional[SecurityCloudAppInfoState | str] = Field(alias="isSupportsSaml", default=None,)
	isTrustedCertificate: Optional[SecurityCloudAppInfoState | str] = Field(alias="isTrustedCertificate", default=None,)
	isUserAuditTrail: Optional[SecurityCloudAppInfoState | str] = Field(alias="isUserAuditTrail", default=None,)
	isUserCanUploadData: Optional[SecurityCloudAppInfoState | str] = Field(alias="isUserCanUploadData", default=None,)
	isUserRolesSupport: Optional[SecurityCloudAppInfoState | str] = Field(alias="isUserRolesSupport", default=None,)
	isValidCertificateName: Optional[SecurityCloudAppInfoState | str] = Field(alias="isValidCertificateName", default=None,)
	latestBreachDateTime: Optional[datetime] = Field(alias="latestBreachDateTime", default=None,)
	logonUrls: Optional[str] = Field(alias="logonUrls", default=None,)
	pciDssVersion: Optional[SecurityAppInfoPciDssVersion | str] = Field(alias="pciDssVersion", default=None,)
	vendor: Optional[str] = Field(alias="vendor", default=None,)

from .security_app_info_csa_star_level import SecurityAppInfoCsaStarLevel
from .security_app_info_data_at_rest_encryption_method import SecurityAppInfoDataAtRestEncryptionMethod
from .security_app_info_data_retention_policy import SecurityAppInfoDataRetentionPolicy
from .security_app_info_uploaded_data_types import SecurityAppInfoUploadedDataTypes
from .security_app_info_encryption_protocol import SecurityAppInfoEncryptionProtocol
from .security_app_info_fed_ramp_level import SecurityAppInfoFedRampLevel
from .security_app_info_holding import SecurityAppInfoHolding
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_cloud_app_info_state import SecurityCloudAppInfoState
from .security_app_info_pci_dss_version import SecurityAppInfoPciDssVersion

