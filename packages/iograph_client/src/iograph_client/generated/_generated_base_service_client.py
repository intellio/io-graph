from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
	from .identity_providers import IdentityProvidersRequest
	from .chats import ChatsRequest
	from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
	from .invitations import InvitationsRequest
	from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
	from .role_management import RoleManagementRequest
	from .information_protection import InformationProtectionRequest
	from .admin import AdminRequest
	from .data_policy_operations import DataPolicyOperationsRequest
	from .domain_dns_records import DomainDnsRecordsRequest
	from .search import SearchRequest
	from .directory import DirectoryRequest
	from .schema_extensions import SchemaExtensionsRequest
	from .teams_templates import TeamsTemplatesRequest
	from .functions import FunctionsRequest
	from .storage import StorageRequest
	from .subscribed_skus import SubscribedSkusRequest
	from .agreements import AgreementsRequest
	from .domains import DomainsRequest
	from .audit_logs import AuditLogsRequest
	from .solutions import SolutionsRequest
	from .application_templates import ApplicationTemplatesRequest
	from .device_app_management import DeviceAppManagementRequest
	from .applications import ApplicationsRequest
	from .identity import IdentityRequest
	from .privacy import PrivacyRequest
	from .places import PlacesRequest
	from .external import ExternalRequest
	from .drives import DrivesRequest
	from .agreement_acceptances import AgreementAcceptancesRequest
	from .employee_experience import EmployeeExperienceRequest
	from .print import PrintRequest
	from .scoped_role_memberships import ScopedRoleMembershipsRequest
	from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
	from .service_principals_with_appid import ServicePrincipalsWithAppIdRequest
	from .organization import OrganizationRequest
	from .sites import SitesRequest
	from .group_settings import GroupSettingsRequest
	from .group_setting_templates import GroupSettingTemplatesRequest
	from .tenant_relationships import TenantRelationshipsRequest
	from .devices import DevicesRequest
	from .groups import GroupsRequest
	from .me import MeRequest
	from .subscriptions import SubscriptionsRequest
	from .devices_with_deviceid import DevicesWithDeviceIdRequest
	from .reports import ReportsRequest
	from .contacts import ContactsRequest
	from .users_with_userprincipalname import UsersWithUserPrincipalNameRequest
	from .planner import PlannerRequest
	from .users import UsersRequest
	from .groups_with_uniquename import GroupsWithUniqueNameRequest
	from .contracts import ContractsRequest
	from .security import SecurityRequest
	from .service_principals import ServicePrincipalsRequest
	from .connections import ConnectionsRequest
	from .communications import CommunicationsRequest
	from .directory_roles_with_roletemplateid import DirectoryRolesWithRoleTemplateIdRequest
	from .permission_grants import PermissionGrantsRequest
	from .teamwork import TeamworkRequest
	from .teams import TeamsRequest
	from .identity_governance import IdentityGovernanceRequest
	from .identity_protection import IdentityProtectionRequest
	from .applications_with_appid import ApplicationsWithAppIdRequest
	from .education import EducationRequest
	from .policies import PoliciesRequest
	from .device_management import DeviceManagementRequest
	from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
	from .authentication_method_configurations import AuthenticationMethodConfigurationsRequest
	from .directory_roles import DirectoryRolesRequest
	from .app_catalogs import AppCatalogsRequest
	from .directory_role_templates import DirectoryRoleTemplatesRequest
	from .shares import SharesRequest
	from .filter_operators import FilterOperatorsRequest
	from .compliance import ComplianceRequest
	from .directory_objects import DirectoryObjectsRequest

class GraphServiceClientBase:

	@property
	def applications_with_uniquename(self) -> ApplicationsWithUniqueNameRequest:
		from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
		return ApplicationsWithUniqueNameRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_providers(self) -> IdentityProvidersRequest:
		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

	@property
	def chats(self) -> ChatsRequest:
		from .chats import ChatsRequest
		return ChatsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_methods_policy(self) -> AuthenticationMethodsPolicyRequest:
		from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
		return AuthenticationMethodsPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def invitations(self) -> InvitationsRequest:
		from .invitations import InvitationsRequest
		return InvitationsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_lifecycle_policies(self) -> GroupLifecyclePoliciesRequest:
		from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
		return GroupLifecyclePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_management(self) -> RoleManagementRequest:
		from .role_management import RoleManagementRequest
		return RoleManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def information_protection(self) -> InformationProtectionRequest:
		from .information_protection import InformationProtectionRequest
		return InformationProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def admin(self) -> AdminRequest:
		from .admin import AdminRequest
		return AdminRequest(self.request_adapter, self.path_parameters)

	@property
	def data_policy_operations(self) -> DataPolicyOperationsRequest:
		from .data_policy_operations import DataPolicyOperationsRequest
		return DataPolicyOperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def domain_dns_records(self) -> DomainDnsRecordsRequest:
		from .domain_dns_records import DomainDnsRecordsRequest
		return DomainDnsRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def search(self) -> SearchRequest:
		from .search import SearchRequest
		return SearchRequest(self.request_adapter, self.path_parameters)

	@property
	def directory(self) -> DirectoryRequest:
		from .directory import DirectoryRequest
		return DirectoryRequest(self.request_adapter, self.path_parameters)

	@property
	def schema_extensions(self) -> SchemaExtensionsRequest:
		from .schema_extensions import SchemaExtensionsRequest
		return SchemaExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def teams_templates(self) -> TeamsTemplatesRequest:
		from .teams_templates import TeamsTemplatesRequest
		return TeamsTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def functions(self) -> FunctionsRequest:
		from .functions import FunctionsRequest
		return FunctionsRequest(self.request_adapter, self.path_parameters)

	@property
	def storage(self) -> StorageRequest:
		from .storage import StorageRequest
		return StorageRequest(self.request_adapter, self.path_parameters)

	@property
	def subscribed_skus(self) -> SubscribedSkusRequest:
		from .subscribed_skus import SubscribedSkusRequest
		return SubscribedSkusRequest(self.request_adapter, self.path_parameters)

	@property
	def agreements(self) -> AgreementsRequest:
		from .agreements import AgreementsRequest
		return AgreementsRequest(self.request_adapter, self.path_parameters)

	@property
	def domains(self) -> DomainsRequest:
		from .domains import DomainsRequest
		return DomainsRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_logs(self) -> AuditLogsRequest:
		from .audit_logs import AuditLogsRequest
		return AuditLogsRequest(self.request_adapter, self.path_parameters)

	@property
	def solutions(self) -> SolutionsRequest:
		from .solutions import SolutionsRequest
		return SolutionsRequest(self.request_adapter, self.path_parameters)

	@property
	def application_templates(self) -> ApplicationTemplatesRequest:
		from .application_templates import ApplicationTemplatesRequest
		return ApplicationTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_app_management(self) -> DeviceAppManagementRequest:
		from .device_app_management import DeviceAppManagementRequest
		return DeviceAppManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def applications(self) -> ApplicationsRequest:
		from .applications import ApplicationsRequest
		return ApplicationsRequest(self.request_adapter, self.path_parameters)

	@property
	def identity(self) -> IdentityRequest:
		from .identity import IdentityRequest
		return IdentityRequest(self.request_adapter, self.path_parameters)

	@property
	def privacy(self) -> PrivacyRequest:
		from .privacy import PrivacyRequest
		return PrivacyRequest(self.request_adapter, self.path_parameters)

	@property
	def places(self) -> PlacesRequest:
		from .places import PlacesRequest
		return PlacesRequest(self.request_adapter, self.path_parameters)

	@property
	def external(self) -> ExternalRequest:
		from .external import ExternalRequest
		return ExternalRequest(self.request_adapter, self.path_parameters)

	@property
	def drives(self) -> DrivesRequest:
		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, self.path_parameters)

	@property
	def agreement_acceptances(self) -> AgreementAcceptancesRequest:
		from .agreement_acceptances import AgreementAcceptancesRequest
		return AgreementAcceptancesRequest(self.request_adapter, self.path_parameters)

	@property
	def employee_experience(self) -> EmployeeExperienceRequest:
		from .employee_experience import EmployeeExperienceRequest
		return EmployeeExperienceRequest(self.request_adapter, self.path_parameters)

	@property
	def print(self) -> PrintRequest:
		from .print import PrintRequest
		return PrintRequest(self.request_adapter, self.path_parameters)

	@property
	def scoped_role_memberships(self) -> ScopedRoleMembershipsRequest:
		from .scoped_role_memberships import ScopedRoleMembershipsRequest
		return ScopedRoleMembershipsRequest(self.request_adapter, self.path_parameters)

	@property
	def oauth2_permission_grants(self) -> Oauth2PermissionGrantsRequest:
		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principals_with_appid(self) -> ServicePrincipalsWithAppIdRequest:
		from .service_principals_with_appid import ServicePrincipalsWithAppIdRequest
		return ServicePrincipalsWithAppIdRequest(self.request_adapter, self.path_parameters)

	@property
	def organization(self) -> OrganizationRequest:
		from .organization import OrganizationRequest
		return OrganizationRequest(self.request_adapter, self.path_parameters)

	@property
	def sites(self) -> SitesRequest:
		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, self.path_parameters)

	@property
	def group_settings(self) -> GroupSettingsRequest:
		from .group_settings import GroupSettingsRequest
		return GroupSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_setting_templates(self) -> GroupSettingTemplatesRequest:
		from .group_setting_templates import GroupSettingTemplatesRequest
		return GroupSettingTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_relationships(self) -> TenantRelationshipsRequest:
		from .tenant_relationships import TenantRelationshipsRequest
		return TenantRelationshipsRequest(self.request_adapter, self.path_parameters)

	@property
	def devices(self) -> DevicesRequest:
		from .devices import DevicesRequest
		return DevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def groups(self) -> GroupsRequest:
		from .groups import GroupsRequest
		return GroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def me(self) -> MeRequest:
		from .me import MeRequest
		return MeRequest(self.request_adapter, self.path_parameters)

	@property
	def subscriptions(self) -> SubscriptionsRequest:
		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

	@property
	def devices_with_deviceid(self) -> DevicesWithDeviceIdRequest:
		from .devices_with_deviceid import DevicesWithDeviceIdRequest
		return DevicesWithDeviceIdRequest(self.request_adapter, self.path_parameters)

	@property
	def reports(self) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def contacts(self) -> ContactsRequest:
		from .contacts import ContactsRequest
		return ContactsRequest(self.request_adapter, self.path_parameters)

	@property
	def users_with_userprincipalname(self) -> UsersWithUserPrincipalNameRequest:
		from .users_with_userprincipalname import UsersWithUserPrincipalNameRequest
		return UsersWithUserPrincipalNameRequest(self.request_adapter, self.path_parameters)

	@property
	def planner(self) -> PlannerRequest:
		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, self.path_parameters)

	@property
	def users(self) -> UsersRequest:
		from .users import UsersRequest
		return UsersRequest(self.request_adapter, self.path_parameters)

	@property
	def groups_with_uniquename(self) -> GroupsWithUniqueNameRequest:
		from .groups_with_uniquename import GroupsWithUniqueNameRequest
		return GroupsWithUniqueNameRequest(self.request_adapter, self.path_parameters)

	@property
	def contracts(self) -> ContractsRequest:
		from .contracts import ContractsRequest
		return ContractsRequest(self.request_adapter, self.path_parameters)

	@property
	def security(self) -> SecurityRequest:
		from .security import SecurityRequest
		return SecurityRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principals(self) -> ServicePrincipalsRequest:
		from .service_principals import ServicePrincipalsRequest
		return ServicePrincipalsRequest(self.request_adapter, self.path_parameters)

	@property
	def connections(self) -> ConnectionsRequest:
		from .connections import ConnectionsRequest
		return ConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def communications(self) -> CommunicationsRequest:
		from .communications import CommunicationsRequest
		return CommunicationsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_roles_with_roletemplateid(self) -> DirectoryRolesWithRoleTemplateIdRequest:
		from .directory_roles_with_roletemplateid import DirectoryRolesWithRoleTemplateIdRequest
		return DirectoryRolesWithRoleTemplateIdRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grants(self) -> PermissionGrantsRequest:
		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def teamwork(self) -> TeamworkRequest:
		from .teamwork import TeamworkRequest
		return TeamworkRequest(self.request_adapter, self.path_parameters)

	@property
	def teams(self) -> TeamsRequest:
		from .teams import TeamsRequest
		return TeamsRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_governance(self) -> IdentityGovernanceRequest:
		from .identity_governance import IdentityGovernanceRequest
		return IdentityGovernanceRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_protection(self) -> IdentityProtectionRequest:
		from .identity_protection import IdentityProtectionRequest
		return IdentityProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def applications_with_appid(self) -> ApplicationsWithAppIdRequest:
		from .applications_with_appid import ApplicationsWithAppIdRequest
		return ApplicationsWithAppIdRequest(self.request_adapter, self.path_parameters)

	@property
	def education(self) -> EducationRequest:
		from .education import EducationRequest
		return EducationRequest(self.request_adapter, self.path_parameters)

	@property
	def policies(self) -> PoliciesRequest:
		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management(self) -> DeviceManagementRequest:
		from .device_management import DeviceManagementRequest
		return DeviceManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_based_auth_configuration(self) -> CertificateBasedAuthConfigurationRequest:
		from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
		return CertificateBasedAuthConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_method_configurations(self) -> AuthenticationMethodConfigurationsRequest:
		from .authentication_method_configurations import AuthenticationMethodConfigurationsRequest
		return AuthenticationMethodConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_roles(self) -> DirectoryRolesRequest:
		from .directory_roles import DirectoryRolesRequest
		return DirectoryRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def app_catalogs(self) -> AppCatalogsRequest:
		from .app_catalogs import AppCatalogsRequest
		return AppCatalogsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_role_templates(self) -> DirectoryRoleTemplatesRequest:
		from .directory_role_templates import DirectoryRoleTemplatesRequest
		return DirectoryRoleTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def shares(self) -> SharesRequest:
		from .shares import SharesRequest
		return SharesRequest(self.request_adapter, self.path_parameters)

	@property
	def filter_operators(self) -> FilterOperatorsRequest:
		from .filter_operators import FilterOperatorsRequest
		return FilterOperatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance(self) -> ComplianceRequest:
		from .compliance import ComplianceRequest
		return ComplianceRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_objects(self) -> DirectoryObjectsRequest:
		from .directory_objects import DirectoryObjectsRequest
		return DirectoryObjectsRequest(self.request_adapter, self.path_parameters)


