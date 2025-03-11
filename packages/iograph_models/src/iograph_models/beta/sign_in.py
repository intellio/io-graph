from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SignIn(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appliedConditionalAccessPolicies: Optional[list[AppliedConditionalAccessPolicy]] = Field(alias="appliedConditionalAccessPolicies",default=None,)
	appliedEventListeners: Optional[list[AppliedAuthenticationEventListener]] = Field(alias="appliedEventListeners",default=None,)
	appOwnerTenantId: Optional[str] = Field(alias="appOwnerTenantId",default=None,)
	appTokenProtectionStatus: Optional[TokenProtectionStatus | str] = Field(alias="appTokenProtectionStatus",default=None,)
	authenticationAppDeviceDetails: Optional[AuthenticationAppDeviceDetails] = Field(alias="authenticationAppDeviceDetails",default=None,)
	authenticationAppPolicyEvaluationDetails: Optional[list[AuthenticationAppPolicyDetails]] = Field(alias="authenticationAppPolicyEvaluationDetails",default=None,)
	authenticationContextClassReferences: Optional[list[AuthenticationContext]] = Field(alias="authenticationContextClassReferences",default=None,)
	authenticationDetails: Optional[list[AuthenticationDetail]] = Field(alias="authenticationDetails",default=None,)
	authenticationMethodsUsed: Optional[list[str]] = Field(alias="authenticationMethodsUsed",default=None,)
	authenticationProcessingDetails: Optional[list[KeyValue]] = Field(alias="authenticationProcessingDetails",default=None,)
	authenticationProtocol: Optional[ProtocolType | str] = Field(alias="authenticationProtocol",default=None,)
	authenticationRequirement: Optional[str] = Field(alias="authenticationRequirement",default=None,)
	authenticationRequirementPolicies: Optional[list[AuthenticationRequirementPolicy]] = Field(alias="authenticationRequirementPolicies",default=None,)
	autonomousSystemNumber: Optional[int] = Field(alias="autonomousSystemNumber",default=None,)
	azureResourceId: Optional[str] = Field(alias="azureResourceId",default=None,)
	clientAppUsed: Optional[str] = Field(alias="clientAppUsed",default=None,)
	clientCredentialType: Optional[ClientCredentialType | str] = Field(alias="clientCredentialType",default=None,)
	conditionalAccessAudiences: Optional[list[str]] = Field(alias="conditionalAccessAudiences",default=None,)
	conditionalAccessStatus: Optional[ConditionalAccessStatus | str] = Field(alias="conditionalAccessStatus",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	crossTenantAccessType: Optional[SignInAccessType | str] = Field(alias="crossTenantAccessType",default=None,)
	deviceDetail: Optional[DeviceDetail] = Field(alias="deviceDetail",default=None,)
	federatedCredentialId: Optional[str] = Field(alias="federatedCredentialId",default=None,)
	flaggedForReview: Optional[bool] = Field(alias="flaggedForReview",default=None,)
	globalSecureAccessIpAddress: Optional[str] = Field(alias="globalSecureAccessIpAddress",default=None,)
	homeTenantId: Optional[str] = Field(alias="homeTenantId",default=None,)
	homeTenantName: Optional[str] = Field(alias="homeTenantName",default=None,)
	incomingTokenType: Optional[IncomingTokenType | str] = Field(alias="incomingTokenType",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	ipAddressFromResourceProvider: Optional[str] = Field(alias="ipAddressFromResourceProvider",default=None,)
	isInteractive: Optional[bool] = Field(alias="isInteractive",default=None,)
	isTenantRestricted: Optional[bool] = Field(alias="isTenantRestricted",default=None,)
	isThroughGlobalSecureAccess: Optional[bool] = Field(alias="isThroughGlobalSecureAccess",default=None,)
	location: Optional[SignInLocation] = Field(alias="location",default=None,)
	managedServiceIdentity: Optional[ManagedIdentity] = Field(alias="managedServiceIdentity",default=None,)
	mfaDetail: Optional[MfaDetail] = Field(alias="mfaDetail",default=None,)
	networkLocationDetails: Optional[list[NetworkLocationDetail]] = Field(alias="networkLocationDetails",default=None,)
	originalRequestId: Optional[str] = Field(alias="originalRequestId",default=None,)
	originalTransferMethod: Optional[OriginalTransferMethods | str] = Field(alias="originalTransferMethod",default=None,)
	privateLinkDetails: Optional[PrivateLinkDetails] = Field(alias="privateLinkDetails",default=None,)
	processingTimeInMilliseconds: Optional[int] = Field(alias="processingTimeInMilliseconds",default=None,)
	resourceDisplayName: Optional[str] = Field(alias="resourceDisplayName",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	resourceOwnerTenantId: Optional[str] = Field(alias="resourceOwnerTenantId",default=None,)
	resourceServicePrincipalId: Optional[str] = Field(alias="resourceServicePrincipalId",default=None,)
	resourceTenantId: Optional[str] = Field(alias="resourceTenantId",default=None,)
	riskDetail: Optional[RiskDetail | str] = Field(alias="riskDetail",default=None,)
	riskEventTypes_v2: Optional[list[str]] = Field(alias="riskEventTypes_v2",default=None,)
	riskLevelAggregated: Optional[RiskLevel | str] = Field(alias="riskLevelAggregated",default=None,)
	riskLevelDuringSignIn: Optional[RiskLevel | str] = Field(alias="riskLevelDuringSignIn",default=None,)
	riskState: Optional[RiskState | str] = Field(alias="riskState",default=None,)
	servicePrincipalCredentialKeyId: Optional[str] = Field(alias="servicePrincipalCredentialKeyId",default=None,)
	servicePrincipalCredentialThumbprint: Optional[str] = Field(alias="servicePrincipalCredentialThumbprint",default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId",default=None,)
	servicePrincipalName: Optional[str] = Field(alias="servicePrincipalName",default=None,)
	sessionId: Optional[str] = Field(alias="sessionId",default=None,)
	sessionLifetimePolicies: Optional[list[SessionLifetimePolicy]] = Field(alias="sessionLifetimePolicies",default=None,)
	signInEventTypes: Optional[list[str]] = Field(alias="signInEventTypes",default=None,)
	signInIdentifier: Optional[str] = Field(alias="signInIdentifier",default=None,)
	signInIdentifierType: Optional[SignInIdentifierType | str] = Field(alias="signInIdentifierType",default=None,)
	signInTokenProtectionStatus: Optional[TokenProtectionStatus | str] = Field(alias="signInTokenProtectionStatus",default=None,)
	status: Optional[SignInStatus] = Field(alias="status",default=None,)
	tokenIssuerName: Optional[str] = Field(alias="tokenIssuerName",default=None,)
	tokenIssuerType: Optional[TokenIssuerType | str] = Field(alias="tokenIssuerType",default=None,)
	tokenProtectionStatusDetails: Optional[TokenProtectionStatusDetails] = Field(alias="tokenProtectionStatusDetails",default=None,)
	uniqueTokenIdentifier: Optional[str] = Field(alias="uniqueTokenIdentifier",default=None,)
	userAgent: Optional[str] = Field(alias="userAgent",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	userType: Optional[SignInUserType | str] = Field(alias="userType",default=None,)

from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
from .applied_authentication_event_listener import AppliedAuthenticationEventListener
from .token_protection_status import TokenProtectionStatus
from .authentication_app_device_details import AuthenticationAppDeviceDetails
from .authentication_app_policy_details import AuthenticationAppPolicyDetails
from .authentication_context import AuthenticationContext
from .authentication_detail import AuthenticationDetail
from .key_value import KeyValue
from .protocol_type import ProtocolType
from .authentication_requirement_policy import AuthenticationRequirementPolicy
from .client_credential_type import ClientCredentialType
from .conditional_access_status import ConditionalAccessStatus
from .sign_in_access_type import SignInAccessType
from .device_detail import DeviceDetail
from .incoming_token_type import IncomingTokenType
from .sign_in_location import SignInLocation
from .managed_identity import ManagedIdentity
from .mfa_detail import MfaDetail
from .network_location_detail import NetworkLocationDetail
from .original_transfer_methods import OriginalTransferMethods
from .private_link_details import PrivateLinkDetails
from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_level import RiskLevel
from .risk_state import RiskState
from .session_lifetime_policy import SessionLifetimePolicy
from .sign_in_identifier_type import SignInIdentifierType
from .token_protection_status import TokenProtectionStatus
from .sign_in_status import SignInStatus
from .token_issuer_type import TokenIssuerType
from .token_protection_status_details import TokenProtectionStatusDetails
from .sign_in_user_type import SignInUserType

