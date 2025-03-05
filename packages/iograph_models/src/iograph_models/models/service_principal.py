from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipal(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	accountEnabled: Optional[bool] = Field(alias="accountEnabled",default=None,)
	addIns: Optional[list[AddIn]] = Field(alias="addIns",default=None,)
	alternativeNames: Optional[list[str]] = Field(alias="alternativeNames",default=None,)
	appDescription: Optional[str] = Field(alias="appDescription",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	applicationTemplateId: Optional[str] = Field(alias="applicationTemplateId",default=None,)
	appOwnerOrganizationId: Optional[UUID] = Field(alias="appOwnerOrganizationId",default=None,)
	appRoleAssignmentRequired: Optional[bool] = Field(alias="appRoleAssignmentRequired",default=None,)
	appRoles: Optional[list[AppRole]] = Field(alias="appRoles",default=None,)
	customSecurityAttributes: Optional[CustomSecurityAttributeValue] = Field(alias="customSecurityAttributes",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	disabledByMicrosoftStatus: Optional[str] = Field(alias="disabledByMicrosoftStatus",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	homepage: Optional[str] = Field(alias="homepage",default=None,)
	info: Optional[InformationalUrl] = Field(alias="info",default=None,)
	keyCredentials: Optional[list[KeyCredential]] = Field(alias="keyCredentials",default=None,)
	loginUrl: Optional[str] = Field(alias="loginUrl",default=None,)
	logoutUrl: Optional[str] = Field(alias="logoutUrl",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	notificationEmailAddresses: Optional[list[str]] = Field(alias="notificationEmailAddresses",default=None,)
	oauth2PermissionScopes: Optional[list[PermissionScope]] = Field(alias="oauth2PermissionScopes",default=None,)
	passwordCredentials: Optional[list[PasswordCredential]] = Field(alias="passwordCredentials",default=None,)
	preferredSingleSignOnMode: Optional[str] = Field(alias="preferredSingleSignOnMode",default=None,)
	preferredTokenSigningKeyThumbprint: Optional[str] = Field(alias="preferredTokenSigningKeyThumbprint",default=None,)
	replyUrls: Optional[list[str]] = Field(alias="replyUrls",default=None,)
	resourceSpecificApplicationPermissions: Optional[list[ResourceSpecificPermission]] = Field(alias="resourceSpecificApplicationPermissions",default=None,)
	samlSingleSignOnSettings: Optional[SamlSingleSignOnSettings] = Field(alias="samlSingleSignOnSettings",default=None,)
	servicePrincipalNames: Optional[list[str]] = Field(alias="servicePrincipalNames",default=None,)
	servicePrincipalType: Optional[str] = Field(alias="servicePrincipalType",default=None,)
	signInAudience: Optional[str] = Field(alias="signInAudience",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	tokenEncryptionKeyId: Optional[UUID] = Field(alias="tokenEncryptionKeyId",default=None,)
	verifiedPublisher: Optional[VerifiedPublisher] = Field(alias="verifiedPublisher",default=None,)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(alias="appManagementPolicies",default=None,)
	appRoleAssignedTo: Optional[list[AppRoleAssignment]] = Field(alias="appRoleAssignedTo",default=None,)
	appRoleAssignments: Optional[list[AppRoleAssignment]] = Field(alias="appRoleAssignments",default=None,)
	claimsMappingPolicies: Optional[list[ClaimsMappingPolicy]] = Field(alias="claimsMappingPolicies",default=None,)
	createdObjects: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="createdObjects",default=None,)
	delegatedPermissionClassifications: Optional[list[DelegatedPermissionClassification]] = Field(alias="delegatedPermissionClassifications",default=None,)
	endpoints: Optional[list[Endpoint]] = Field(alias="endpoints",default=None,)
	federatedIdentityCredentials: Optional[list[FederatedIdentityCredential]] = Field(alias="federatedIdentityCredentials",default=None,)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(alias="homeRealmDiscoveryPolicies",default=None,)
	memberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="memberOf",default=None,)
	oauth2PermissionGrants: Optional[list[OAuth2PermissionGrant]] = Field(alias="oauth2PermissionGrants",default=None,)
	ownedObjects: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="ownedObjects",default=None,)
	owners: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="owners",default=None,)
	remoteDesktopSecurityConfiguration: Optional[RemoteDesktopSecurityConfiguration] = Field(alias="remoteDesktopSecurityConfiguration",default=None,)
	synchronization: Optional[Synchronization] = Field(alias="synchronization",default=None,)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(alias="tokenIssuancePolicies",default=None,)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(alias="tokenLifetimePolicies",default=None,)
	transitiveMemberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="transitiveMemberOf",default=None,)

from .add_in import AddIn
from .app_role import AppRole
from .custom_security_attribute_value import CustomSecurityAttributeValue
from .informational_url import InformationalUrl
from .key_credential import KeyCredential
from .permission_scope import PermissionScope
from .password_credential import PasswordCredential
from .resource_specific_permission import ResourceSpecificPermission
from .saml_single_sign_on_settings import SamlSingleSignOnSettings
from .verified_publisher import VerifiedPublisher
from .app_management_policy import AppManagementPolicy
from .app_role_assignment import AppRoleAssignment
from .app_role_assignment import AppRoleAssignment
from .claims_mapping_policy import ClaimsMappingPolicy
from .directory_object import DirectoryObject
from .delegated_permission_classification import DelegatedPermissionClassification
from .endpoint import Endpoint
from .federated_identity_credential import FederatedIdentityCredential
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .directory_object import DirectoryObject
from .o_auth2_permission_grant import OAuth2PermissionGrant
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
from .synchronization import Synchronization
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .directory_object import DirectoryObject

