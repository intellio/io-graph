from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class HealthMonitoringDirectoryObjectImpactSummary(BaseModel):
	impactedCount: Optional[str] = Field(alias="impactedCount", default=None,)
	impactedCountLimitExceeded: Optional[bool] = Field(alias="impactedCountLimitExceeded", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	odata_type: Literal["#microsoft.graph.healthMonitoring.directoryObjectImpactSummary"] = Field(alias="@odata.type", default="#microsoft.graph.healthMonitoring.directoryObjectImpactSummary")
	resourceSampling: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="resourceSampling", default=None,)

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
			if mapping_key == "#microsoft.graph.healthMonitoring.applicationImpactSummary":
				from .health_monitoring_application_impact_summary import HealthMonitoringApplicationImpactSummary
				return HealthMonitoringApplicationImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.deviceImpactSummary":
				from .health_monitoring_device_impact_summary import HealthMonitoringDeviceImpactSummary
				return HealthMonitoringDeviceImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.groupImpactSummary":
				from .health_monitoring_group_impact_summary import HealthMonitoringGroupImpactSummary
				return HealthMonitoringGroupImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.servicePrincipalImpactSummary":
				from .health_monitoring_service_principal_impact_summary import HealthMonitoringServicePrincipalImpactSummary
				return HealthMonitoringServicePrincipalImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.userImpactSummary":
				from .health_monitoring_user_impact_summary import HealthMonitoringUserImpactSummary
				return HealthMonitoringUserImpactSummary.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .administrative_unit import AdministrativeUnit
from .application import Application
from .app_role_assignment import AppRoleAssignment
from .certificate_authority_detail import CertificateAuthorityDetail
from .certificate_based_auth_pki import CertificateBasedAuthPki
from .contract import Contract
from .device import Device
from .device_template import DeviceTemplate
from .directory_object_partner_reference import DirectoryObjectPartnerReference
from .directory_role import DirectoryRole
from .directory_role_template import DirectoryRoleTemplate
from .directory_setting_template import DirectorySettingTemplate
from .endpoint import Endpoint
from .extension_property import ExtensionProperty
from .external_user_profile import ExternalUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
from .federated_token_validation_policy import FederatedTokenValidationPolicy
from .group import Group
from .mailbox import Mailbox
from .multi_tenant_organization_member import MultiTenantOrganizationMember
from .organization import Organization
from .org_contact import OrgContact
from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .external_identities_policy import ExternalIdentitiesPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .service_principal_creation_policy import ServicePrincipalCreationPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
from .user import User
