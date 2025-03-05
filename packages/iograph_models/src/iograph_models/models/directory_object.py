from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryObject(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.administrativeUnit":
				from .administrative_unit import AdministrativeUnit
				return AdministrativeUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.application":
				from .application import Application
				return Application.model_validate(data)
			if mapping_key == "#microsoft.graph.appRoleAssignment":
				from .app_role_assignment import AppRoleAssignment
				return AppRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.contract":
				from .contract import Contract
				return Contract.model_validate(data)
			if mapping_key == "#microsoft.graph.device":
				from .device import Device
				return Device.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryObjectPartnerReference":
				from .directory_object_partner_reference import DirectoryObjectPartnerReference
				return DirectoryObjectPartnerReference.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRole":
				from .directory_role import DirectoryRole
				return DirectoryRole.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRoleTemplate":
				from .directory_role_template import DirectoryRoleTemplate
				return DirectoryRoleTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.endpoint":
				from .endpoint import Endpoint
				return Endpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.extensionProperty":
				from .extension_property import ExtensionProperty
				return ExtensionProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.group":
				from .group import Group
				return Group.model_validate(data)
			if mapping_key == "#microsoft.graph.groupSettingTemplate":
				from .group_setting_template import GroupSettingTemplate
				return GroupSettingTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationMember":
				from .multi_tenant_organization_member import MultiTenantOrganizationMember
				return MultiTenantOrganizationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.organization":
				from .organization import Organization
				return Organization.model_validate(data)
			if mapping_key == "#microsoft.graph.orgContact":
				from .org_contact import OrgContact
				return OrgContact.model_validate(data)
			if mapping_key == "#microsoft.graph.policyBase":
				from .policy_base import PolicyBase
				return PolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.appManagementPolicy":
				from .app_management_policy import AppManagementPolicy
				return AppManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationPolicy":
				from .authorization_policy import AuthorizationPolicy
				return AuthorizationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.crossTenantAccessPolicy":
				from .cross_tenant_access_policy import CrossTenantAccessPolicy
				return CrossTenantAccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
				from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
				return IdentitySecurityDefaultsEnforcementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantPolicy":
				from .permission_grant_policy import PermissionGrantPolicy
				return PermissionGrantPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.stsPolicy":
				from .sts_policy import StsPolicy
				return StsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.activityBasedTimeoutPolicy":
				from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
				return ActivityBasedTimeoutPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.claimsMappingPolicy":
				from .claims_mapping_policy import ClaimsMappingPolicy
				return ClaimsMappingPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.homeRealmDiscoveryPolicy":
				from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
				return HomeRealmDiscoveryPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenIssuancePolicy":
				from .token_issuance_policy import TokenIssuancePolicy
				return TokenIssuancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenLifetimePolicy":
				from .token_lifetime_policy import TokenLifetimePolicy
				return TokenLifetimePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tenantAppManagementPolicy":
				from .tenant_app_management_policy import TenantAppManagementPolicy
				return TenantAppManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.resourceSpecificPermissionGrant":
				from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
				return ResourceSpecificPermissionGrant.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipal":
				from .service_principal import ServicePrincipal
				return ServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.user":
				from .user import User
				return User.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


