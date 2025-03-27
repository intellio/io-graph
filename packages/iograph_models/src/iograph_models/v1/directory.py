from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Directory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	administrativeUnits: Optional[list[AdministrativeUnit]] = Field(alias="administrativeUnits", default=None,)
	attributeSets: Optional[list[AttributeSet]] = Field(alias="attributeSets", default=None,)
	customSecurityAttributeDefinitions: Optional[list[CustomSecurityAttributeDefinition]] = Field(alias="customSecurityAttributeDefinitions", default=None,)
	deletedItems: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="deletedItems", default=None,)
	deviceLocalCredentials: Optional[list[DeviceLocalCredentialInfo]] = Field(alias="deviceLocalCredentials", default=None,)
	federationConfigurations: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, SamlOrWsFedProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider],Field(discriminator="odata_type")]]] = Field(alias="federationConfigurations", default=None,)
	onPremisesSynchronization: Optional[list[OnPremisesDirectorySynchronization]] = Field(alias="onPremisesSynchronization", default=None,)
	subscriptions: Optional[list[CompanySubscription]] = Field(alias="subscriptions", default=None,)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
from .administrative_unit import AdministrativeUnit
from .application import Application
from .app_role_assignment import AppRoleAssignment
from .contract import Contract
from .device import Device
from .directory_object_partner_reference import DirectoryObjectPartnerReference
from .directory_role import DirectoryRole
from .directory_role_template import DirectoryRoleTemplate
from .endpoint import Endpoint
from .extension_property import ExtensionProperty
from .group import Group
from .group_setting_template import GroupSettingTemplate
from .multi_tenant_organization_member import MultiTenantOrganizationMember
from .organization import Organization
from .org_contact import OrgContact
from .policy_base import PolicyBase
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .sts_policy import StsPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .user import User
from .device_local_credential_info import DeviceLocalCredentialInfo
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .saml_or_ws_fed_provider import SamlOrWsFedProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .company_subscription import CompanySubscription

