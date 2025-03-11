from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Application(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	api: Optional[ApiApplication] = Field(alias="api",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appRoles: Optional[list[AppRole]] = Field(alias="appRoles",default=None,)
	authenticationBehaviors: Optional[AuthenticationBehaviors] = Field(alias="authenticationBehaviors",default=None,)
	certification: Optional[Certification] = Field(alias="certification",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	defaultRedirectUri: Optional[str] = Field(alias="defaultRedirectUri",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	disabledByMicrosoftStatus: Optional[str] = Field(alias="disabledByMicrosoftStatus",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	groupMembershipClaims: Optional[str] = Field(alias="groupMembershipClaims",default=None,)
	identifierUris: Optional[list[str]] = Field(alias="identifierUris",default=None,)
	info: Optional[InformationalUrl] = Field(alias="info",default=None,)
	isDeviceOnlyAuthSupported: Optional[bool] = Field(alias="isDeviceOnlyAuthSupported",default=None,)
	isFallbackPublicClient: Optional[bool] = Field(alias="isFallbackPublicClient",default=None,)
	keyCredentials: Optional[list[KeyCredential]] = Field(alias="keyCredentials",default=None,)
	logo: Optional[str] = Field(alias="logo",default=None,)
	nativeAuthenticationApisEnabled: Optional[NativeAuthenticationApisEnabled | str] = Field(alias="nativeAuthenticationApisEnabled",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	onPremisesPublishing: Optional[OnPremisesPublishing] = Field(alias="onPremisesPublishing",default=None,)
	optionalClaims: Optional[OptionalClaims] = Field(alias="optionalClaims",default=None,)
	parentalControlSettings: Optional[ParentalControlSettings] = Field(alias="parentalControlSettings",default=None,)
	passwordCredentials: Optional[list[PasswordCredential]] = Field(alias="passwordCredentials",default=None,)
	publicClient: Optional[PublicClientApplication] = Field(alias="publicClient",default=None,)
	publisherDomain: Optional[str] = Field(alias="publisherDomain",default=None,)
	requestSignatureVerification: Optional[RequestSignatureVerification] = Field(alias="requestSignatureVerification",default=None,)
	requiredResourceAccess: Optional[list[RequiredResourceAccess]] = Field(alias="requiredResourceAccess",default=None,)
	samlMetadataUrl: Optional[str] = Field(alias="samlMetadataUrl",default=None,)
	serviceManagementReference: Optional[str] = Field(alias="serviceManagementReference",default=None,)
	servicePrincipalLockConfiguration: Optional[ServicePrincipalLockConfiguration] = Field(alias="servicePrincipalLockConfiguration",default=None,)
	signInAudience: Optional[str] = Field(alias="signInAudience",default=None,)
	spa: Optional[SpaApplication] = Field(alias="spa",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	tokenEncryptionKeyId: Optional[UUID] = Field(alias="tokenEncryptionKeyId",default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName",default=None,)
	verifiedPublisher: Optional[VerifiedPublisher] = Field(alias="verifiedPublisher",default=None,)
	web: Optional[WebApplication] = Field(alias="web",default=None,)
	windows: Optional[WindowsApplication] = Field(alias="windows",default=None,)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(alias="appManagementPolicies",default=None,)
	connectorGroup: Optional[ConnectorGroup] = Field(alias="connectorGroup",default=None,)
	createdOnBehalfOf: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="createdOnBehalfOf",default=None,)
	extensionProperties: Optional[list[ExtensionProperty]] = Field(alias="extensionProperties",default=None,)
	federatedIdentityCredentials: Optional[list[FederatedIdentityCredential]] = Field(alias="federatedIdentityCredentials",default=None,)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(alias="homeRealmDiscoveryPolicies",default=None,)
	owners: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="owners",default=None,)
	synchronization: Optional[Synchronization] = Field(alias="synchronization",default=None,)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(alias="tokenIssuancePolicies",default=None,)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(alias="tokenLifetimePolicies",default=None,)

from .api_application import ApiApplication
from .app_role import AppRole
from .authentication_behaviors import AuthenticationBehaviors
from .certification import Certification
from .informational_url import InformationalUrl
from .key_credential import KeyCredential
from .native_authentication_apis_enabled import NativeAuthenticationApisEnabled
from .on_premises_publishing import OnPremisesPublishing
from .optional_claims import OptionalClaims
from .parental_control_settings import ParentalControlSettings
from .password_credential import PasswordCredential
from .public_client_application import PublicClientApplication
from .request_signature_verification import RequestSignatureVerification
from .required_resource_access import RequiredResourceAccess
from .service_principal_lock_configuration import ServicePrincipalLockConfiguration
from .spa_application import SpaApplication
from .verified_publisher import VerifiedPublisher
from .web_application import WebApplication
from .windows_application import WindowsApplication
from .app_management_policy import AppManagementPolicy
from .connector_group import ConnectorGroup
from .directory_object import DirectoryObject
from .extension_property import ExtensionProperty
from .federated_identity_credential import FederatedIdentityCredential
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .directory_object import DirectoryObject
from .synchronization import Synchronization
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy

