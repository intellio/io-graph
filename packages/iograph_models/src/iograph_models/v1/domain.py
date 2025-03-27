from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Domain(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authenticationType: Optional[str] = Field(alias="authenticationType", default=None,)
	availabilityStatus: Optional[str] = Field(alias="availabilityStatus", default=None,)
	isAdminManaged: Optional[bool] = Field(alias="isAdminManaged", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isInitial: Optional[bool] = Field(alias="isInitial", default=None,)
	isRoot: Optional[bool] = Field(alias="isRoot", default=None,)
	isVerified: Optional[bool] = Field(alias="isVerified", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	passwordNotificationWindowInDays: Optional[int] = Field(alias="passwordNotificationWindowInDays", default=None,)
	passwordValidityPeriodInDays: Optional[int] = Field(alias="passwordValidityPeriodInDays", default=None,)
	state: Optional[DomainState] = Field(alias="state", default=None,)
	supportedServices: Optional[list[str]] = Field(alias="supportedServices", default=None,)
	domainNameReferences: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="domainNameReferences", default=None,)
	federationConfiguration: Optional[list[InternalDomainFederation]] = Field(alias="federationConfiguration", default=None,)
	rootDomain: Optional[Domain] = Field(alias="rootDomain", default=None,)
	serviceConfigurationRecords: Optional[list[Annotated[Union[DomainDnsCnameRecord, DomainDnsMxRecord, DomainDnsSrvRecord, DomainDnsTxtRecord, DomainDnsUnavailableRecord]],Field(discriminator="odata_type")]]] = Field(alias="serviceConfigurationRecords", default=None,)
	verificationDnsRecords: Optional[list[Annotated[Union[DomainDnsCnameRecord, DomainDnsMxRecord, DomainDnsSrvRecord, DomainDnsTxtRecord, DomainDnsUnavailableRecord]],Field(discriminator="odata_type")]]] = Field(alias="verificationDnsRecords", default=None,)

from .domain_state import DomainState
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
from .internal_domain_federation import InternalDomainFederation
from .domain_dns_cname_record import DomainDnsCnameRecord
from .domain_dns_mx_record import DomainDnsMxRecord
from .domain_dns_srv_record import DomainDnsSrvRecord
from .domain_dns_txt_record import DomainDnsTxtRecord
from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
from .domain_dns_cname_record import DomainDnsCnameRecord
from .domain_dns_mx_record import DomainDnsMxRecord
from .domain_dns_srv_record import DomainDnsSrvRecord
from .domain_dns_txt_record import DomainDnsTxtRecord
from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

