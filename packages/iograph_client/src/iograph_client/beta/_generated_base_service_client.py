from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .reports import ReportsRequest
	from .term_store import TermStoreRequest
	from .education import EducationRequest
	from .applications_with_appid import ApplicationsWithAppIdRequest
	from .financials import FinancialsRequest
	from .application_templates import ApplicationTemplatesRequest
	from .places import PlacesRequest
	from .subscriptions import SubscriptionsRequest
	from .identity_providers import IdentityProvidersRequest
	from .message_traces import MessageTracesRequest
	from .commands import CommandsRequest
	from .mobility_management_policies import MobilityManagementPoliciesRequest
	from .device_management import DeviceManagementRequest
	from .risk_detections import RiskDetectionsRequest
	from .search import SearchRequest
	from .devices import DevicesRequest
	from .filter_operators import FilterOperatorsRequest
	from .external import ExternalRequest
	from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
	from .trust_framework import TrustFrameworkRequest
	from .teams_templates import TeamsTemplatesRequest
	from .tenant_relationships import TenantRelationshipsRequest
	from .authentication_method_devices import AuthenticationMethodDevicesRequest
	from .invitations import InvitationsRequest
	from .admin import AdminRequest
	from .privileged_operation_events import PrivilegedOperationEventsRequest
	from .filtering_policies import FilteringPoliciesRequest
	from .app_catalogs import AppCatalogsRequest
	from .schema_extensions import SchemaExtensionsRequest
	from .threat_submission import ThreatSubmissionRequest
	from .approval_workflow_providers import ApprovalWorkflowProvidersRequest
	from .governance_role_definitions import GovernanceRoleDefinitionsRequest
	from .contracts import ContractsRequest
	from .booking_currencies import BookingCurrenciesRequest
	from .privileged_access import PrivilegedAccessRequest
	from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
	from .information_protection import InformationProtectionRequest
	from .policies import PoliciesRequest
	from .chats import ChatsRequest
	from .privileged_approval import PrivilegedApprovalRequest
	from .groups_with_uniquename import GroupsWithUniqueNameRequest
	from .templates import TemplatesRequest
	from .network_access import NetworkAccessRequest
	from .drives import DrivesRequest
	from .security import SecurityRequest
	from .service_principals import ServicePrincipalsRequest
	from .communications import CommunicationsRequest
	from .activitystatistics import ActivitystatisticsRequest
	from .directory_roles_with_roletemplateid import DirectoryRolesWithRoleTemplateIdRequest
	from .teams import TeamsRequest
	from .agreements import AgreementsRequest
	from .shares import SharesRequest
	from .data_policy_operations import DataPolicyOperationsRequest
	from .governance_resources import GovernanceResourcesRequest
	from .program_control_types import ProgramControlTypesRequest
	from .governance_subjects import GovernanceSubjectsRequest
	from .planner import PlannerRequest
	from .settings import SettingsRequest
	from .governance_role_assignment_requests import GovernanceRoleAssignmentRequestsRequest
	from .on_premises_publishing_profiles import OnPremisesPublishingProfilesRequest
	from .privileged_signup_status import PrivilegedSignupStatusRequest
	from .risky_users import RiskyUsersRequest
	from .workplace import WorkplaceRequest
	from .copilot import CopilotRequest
	from .program_controls import ProgramControlsRequest
	from .administrative_units import AdministrativeUnitsRequest
	from .access_reviews import AccessReviewsRequest
	from .certificate_authorities import CertificateAuthoritiesRequest
	from .service_principals_with_appid import ServicePrincipalsWithAppIdRequest
	from .connections import ConnectionsRequest
	from .sites import SitesRequest
	from .booking_businesses import BookingBusinessesRequest
	from .teamwork import TeamworkRequest
	from .access_review_decisions import AccessReviewDecisionsRequest
	from .directory_setting_templates import DirectorySettingTemplatesRequest
	from .data_classification import DataClassificationRequest
	from .monitoring import MonitoringRequest
	from .contacts import ContactsRequest
	from .scoped_role_memberships import ScopedRoleMembershipsRequest
	from .agreement_acceptances import AgreementAcceptancesRequest
	from .authentication_method_configurations import AuthenticationMethodConfigurationsRequest
	from .me import MeRequest
	from .privacy import PrivacyRequest
	from .devices_with_deviceid import DevicesWithDeviceIdRequest
	from .allowed_data_locations import AllowedDataLocationsRequest
	from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
	from .privileged_role_assignments import PrivilegedRoleAssignmentsRequest
	from .permission_grants import PermissionGrantsRequest
	from .storage import StorageRequest
	from .identity import IdentityRequest
	from .solutions import SolutionsRequest
	from .directory_objects import DirectoryObjectsRequest
	from .organization import OrganizationRequest
	from .business_flow_templates import BusinessFlowTemplatesRequest
	from .app import AppRequest
	from .users_with_userprincipalname import UsersWithUserPrincipalNameRequest
	from .role_management import RoleManagementRequest
	from .payload_response import PayloadResponseRequest
	from .functions import FunctionsRequest
	from .message_events import MessageEventsRequest
	from .subscribed_skus import SubscribedSkusRequest
	from .privileged_role_assignment_requests import PrivilegedRoleAssignmentRequestsRequest
	from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
	from .governance_role_assignments import GovernanceRoleAssignmentsRequest
	from .network import NetworkRequest
	from .identity_protection import IdentityProtectionRequest
	from .employee_experience import EmployeeExperienceRequest
	from .team_template_definition import TeamTemplateDefinitionRequest
	from .directory_roles import DirectoryRolesRequest
	from .directory import DirectoryRequest
	from .message_recipients import MessageRecipientsRequest
	from .print import PrintRequest
	from .privileged_roles import PrivilegedRolesRequest
	from .programs import ProgramsRequest
	from .identity_governance import IdentityGovernanceRequest
	from .compliance import ComplianceRequest
	from .groups import GroupsRequest
	from .places_with_placeid import PlacesWithPlaceIdRequest
	from .governance_role_settings import GovernanceRoleSettingsRequest
	from .device_app_management import DeviceAppManagementRequest
	from .directory_role_templates import DirectoryRoleTemplatesRequest
	from .domain_dns_records import DomainDnsRecordsRequest
	from .audit_logs import AuditLogsRequest
	from .users import UsersRequest
	from .applications import ApplicationsRequest
	from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
	from .domains import DomainsRequest

class GraphServiceClientBase:

	@property
	def reports(self) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def term_store(self) -> TermStoreRequest:
		from .term_store import TermStoreRequest
		return TermStoreRequest(self.request_adapter, self.path_parameters)

	@property
	def education(self) -> EducationRequest:
		from .education import EducationRequest
		return EducationRequest(self.request_adapter, self.path_parameters)

	@property
	def applications_with_appid(self) -> ApplicationsWithAppIdRequest:
		from .applications_with_appid import ApplicationsWithAppIdRequest
		return ApplicationsWithAppIdRequest(self.request_adapter, self.path_parameters)

	@property
	def financials(self) -> FinancialsRequest:
		from .financials import FinancialsRequest
		return FinancialsRequest(self.request_adapter, self.path_parameters)

	@property
	def application_templates(self) -> ApplicationTemplatesRequest:
		from .application_templates import ApplicationTemplatesRequest
		return ApplicationTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def places(self) -> PlacesRequest:
		from .places import PlacesRequest
		return PlacesRequest(self.request_adapter, self.path_parameters)

	@property
	def subscriptions(self) -> SubscriptionsRequest:
		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_providers(self) -> IdentityProvidersRequest:
		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

	@property
	def message_traces(self) -> MessageTracesRequest:
		from .message_traces import MessageTracesRequest
		return MessageTracesRequest(self.request_adapter, self.path_parameters)

	@property
	def commands(self) -> CommandsRequest:
		from .commands import CommandsRequest
		return CommandsRequest(self.request_adapter, self.path_parameters)

	@property
	def mobility_management_policies(self) -> MobilityManagementPoliciesRequest:
		from .mobility_management_policies import MobilityManagementPoliciesRequest
		return MobilityManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management(self) -> DeviceManagementRequest:
		from .device_management import DeviceManagementRequest
		return DeviceManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def risk_detections(self) -> RiskDetectionsRequest:
		from .risk_detections import RiskDetectionsRequest
		return RiskDetectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def search(self) -> SearchRequest:
		from .search import SearchRequest
		return SearchRequest(self.request_adapter, self.path_parameters)

	@property
	def devices(self) -> DevicesRequest:
		from .devices import DevicesRequest
		return DevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def filter_operators(self) -> FilterOperatorsRequest:
		from .filter_operators import FilterOperatorsRequest
		return FilterOperatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def external(self) -> ExternalRequest:
		from .external import ExternalRequest
		return ExternalRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_methods_policy(self) -> AuthenticationMethodsPolicyRequest:
		from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
		return AuthenticationMethodsPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def trust_framework(self) -> TrustFrameworkRequest:
		from .trust_framework import TrustFrameworkRequest
		return TrustFrameworkRequest(self.request_adapter, self.path_parameters)

	@property
	def teams_templates(self) -> TeamsTemplatesRequest:
		from .teams_templates import TeamsTemplatesRequest
		return TeamsTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_relationships(self) -> TenantRelationshipsRequest:
		from .tenant_relationships import TenantRelationshipsRequest
		return TenantRelationshipsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_method_devices(self) -> AuthenticationMethodDevicesRequest:
		from .authentication_method_devices import AuthenticationMethodDevicesRequest
		return AuthenticationMethodDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def invitations(self) -> InvitationsRequest:
		from .invitations import InvitationsRequest
		return InvitationsRequest(self.request_adapter, self.path_parameters)

	@property
	def admin(self) -> AdminRequest:
		from .admin import AdminRequest
		return AdminRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_operation_events(self) -> PrivilegedOperationEventsRequest:
		from .privileged_operation_events import PrivilegedOperationEventsRequest
		return PrivilegedOperationEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def filtering_policies(self) -> FilteringPoliciesRequest:
		from .filtering_policies import FilteringPoliciesRequest
		return FilteringPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def app_catalogs(self) -> AppCatalogsRequest:
		from .app_catalogs import AppCatalogsRequest
		return AppCatalogsRequest(self.request_adapter, self.path_parameters)

	@property
	def schema_extensions(self) -> SchemaExtensionsRequest:
		from .schema_extensions import SchemaExtensionsRequest
		return SchemaExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def threat_submission(self) -> ThreatSubmissionRequest:
		from .threat_submission import ThreatSubmissionRequest
		return ThreatSubmissionRequest(self.request_adapter, self.path_parameters)

	@property
	def approval_workflow_providers(self) -> ApprovalWorkflowProvidersRequest:
		from .approval_workflow_providers import ApprovalWorkflowProvidersRequest
		return ApprovalWorkflowProvidersRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_role_definitions(self) -> GovernanceRoleDefinitionsRequest:
		from .governance_role_definitions import GovernanceRoleDefinitionsRequest
		return GovernanceRoleDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def contracts(self) -> ContractsRequest:
		from .contracts import ContractsRequest
		return ContractsRequest(self.request_adapter, self.path_parameters)

	@property
	def booking_currencies(self) -> BookingCurrenciesRequest:
		from .booking_currencies import BookingCurrenciesRequest
		return BookingCurrenciesRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_access(self) -> PrivilegedAccessRequest:
		from .privileged_access import PrivilegedAccessRequest
		return PrivilegedAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def applications_with_uniquename(self) -> ApplicationsWithUniqueNameRequest:
		from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
		return ApplicationsWithUniqueNameRequest(self.request_adapter, self.path_parameters)

	@property
	def information_protection(self) -> InformationProtectionRequest:
		from .information_protection import InformationProtectionRequest
		return InformationProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def policies(self) -> PoliciesRequest:
		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def chats(self) -> ChatsRequest:
		from .chats import ChatsRequest
		return ChatsRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_approval(self) -> PrivilegedApprovalRequest:
		from .privileged_approval import PrivilegedApprovalRequest
		return PrivilegedApprovalRequest(self.request_adapter, self.path_parameters)

	@property
	def groups_with_uniquename(self) -> GroupsWithUniqueNameRequest:
		from .groups_with_uniquename import GroupsWithUniqueNameRequest
		return GroupsWithUniqueNameRequest(self.request_adapter, self.path_parameters)

	@property
	def templates(self) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def network_access(self) -> NetworkAccessRequest:
		from .network_access import NetworkAccessRequest
		return NetworkAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def drives(self) -> DrivesRequest:
		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, self.path_parameters)

	@property
	def security(self) -> SecurityRequest:
		from .security import SecurityRequest
		return SecurityRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principals(self) -> ServicePrincipalsRequest:
		from .service_principals import ServicePrincipalsRequest
		return ServicePrincipalsRequest(self.request_adapter, self.path_parameters)

	@property
	def communications(self) -> CommunicationsRequest:
		from .communications import CommunicationsRequest
		return CommunicationsRequest(self.request_adapter, self.path_parameters)

	@property
	def activitystatistics(self) -> ActivitystatisticsRequest:
		from .activitystatistics import ActivitystatisticsRequest
		return ActivitystatisticsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_roles_with_roletemplateid(self) -> DirectoryRolesWithRoleTemplateIdRequest:
		from .directory_roles_with_roletemplateid import DirectoryRolesWithRoleTemplateIdRequest
		return DirectoryRolesWithRoleTemplateIdRequest(self.request_adapter, self.path_parameters)

	@property
	def teams(self) -> TeamsRequest:
		from .teams import TeamsRequest
		return TeamsRequest(self.request_adapter, self.path_parameters)

	@property
	def agreements(self) -> AgreementsRequest:
		from .agreements import AgreementsRequest
		return AgreementsRequest(self.request_adapter, self.path_parameters)

	@property
	def shares(self) -> SharesRequest:
		from .shares import SharesRequest
		return SharesRequest(self.request_adapter, self.path_parameters)

	@property
	def data_policy_operations(self) -> DataPolicyOperationsRequest:
		from .data_policy_operations import DataPolicyOperationsRequest
		return DataPolicyOperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_resources(self) -> GovernanceResourcesRequest:
		from .governance_resources import GovernanceResourcesRequest
		return GovernanceResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def program_control_types(self) -> ProgramControlTypesRequest:
		from .program_control_types import ProgramControlTypesRequest
		return ProgramControlTypesRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_subjects(self) -> GovernanceSubjectsRequest:
		from .governance_subjects import GovernanceSubjectsRequest
		return GovernanceSubjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def planner(self) -> PlannerRequest:
		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_role_assignment_requests(self) -> GovernanceRoleAssignmentRequestsRequest:
		from .governance_role_assignment_requests import GovernanceRoleAssignmentRequestsRequest
		return GovernanceRoleAssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def on_premises_publishing_profiles(self) -> OnPremisesPublishingProfilesRequest:
		from .on_premises_publishing_profiles import OnPremisesPublishingProfilesRequest
		return OnPremisesPublishingProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_signup_status(self) -> PrivilegedSignupStatusRequest:
		from .privileged_signup_status import PrivilegedSignupStatusRequest
		return PrivilegedSignupStatusRequest(self.request_adapter, self.path_parameters)

	@property
	def risky_users(self) -> RiskyUsersRequest:
		from .risky_users import RiskyUsersRequest
		return RiskyUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def workplace(self) -> WorkplaceRequest:
		from .workplace import WorkplaceRequest
		return WorkplaceRequest(self.request_adapter, self.path_parameters)

	@property
	def copilot(self) -> CopilotRequest:
		from .copilot import CopilotRequest
		return CopilotRequest(self.request_adapter, self.path_parameters)

	@property
	def program_controls(self) -> ProgramControlsRequest:
		from .program_controls import ProgramControlsRequest
		return ProgramControlsRequest(self.request_adapter, self.path_parameters)

	@property
	def administrative_units(self) -> AdministrativeUnitsRequest:
		from .administrative_units import AdministrativeUnitsRequest
		return AdministrativeUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_reviews(self) -> AccessReviewsRequest:
		from .access_reviews import AccessReviewsRequest
		return AccessReviewsRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_authorities(self) -> CertificateAuthoritiesRequest:
		from .certificate_authorities import CertificateAuthoritiesRequest
		return CertificateAuthoritiesRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principals_with_appid(self) -> ServicePrincipalsWithAppIdRequest:
		from .service_principals_with_appid import ServicePrincipalsWithAppIdRequest
		return ServicePrincipalsWithAppIdRequest(self.request_adapter, self.path_parameters)

	@property
	def connections(self) -> ConnectionsRequest:
		from .connections import ConnectionsRequest
		return ConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def sites(self) -> SitesRequest:
		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, self.path_parameters)

	@property
	def booking_businesses(self) -> BookingBusinessesRequest:
		from .booking_businesses import BookingBusinessesRequest
		return BookingBusinessesRequest(self.request_adapter, self.path_parameters)

	@property
	def teamwork(self) -> TeamworkRequest:
		from .teamwork import TeamworkRequest
		return TeamworkRequest(self.request_adapter, self.path_parameters)

	@property
	def access_review_decisions(self) -> AccessReviewDecisionsRequest:
		from .access_review_decisions import AccessReviewDecisionsRequest
		return AccessReviewDecisionsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_setting_templates(self) -> DirectorySettingTemplatesRequest:
		from .directory_setting_templates import DirectorySettingTemplatesRequest
		return DirectorySettingTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def data_classification(self) -> DataClassificationRequest:
		from .data_classification import DataClassificationRequest
		return DataClassificationRequest(self.request_adapter, self.path_parameters)

	@property
	def monitoring(self) -> MonitoringRequest:
		from .monitoring import MonitoringRequest
		return MonitoringRequest(self.request_adapter, self.path_parameters)

	@property
	def contacts(self) -> ContactsRequest:
		from .contacts import ContactsRequest
		return ContactsRequest(self.request_adapter, self.path_parameters)

	@property
	def scoped_role_memberships(self) -> ScopedRoleMembershipsRequest:
		from .scoped_role_memberships import ScopedRoleMembershipsRequest
		return ScopedRoleMembershipsRequest(self.request_adapter, self.path_parameters)

	@property
	def agreement_acceptances(self) -> AgreementAcceptancesRequest:
		from .agreement_acceptances import AgreementAcceptancesRequest
		return AgreementAcceptancesRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_method_configurations(self) -> AuthenticationMethodConfigurationsRequest:
		from .authentication_method_configurations import AuthenticationMethodConfigurationsRequest
		return AuthenticationMethodConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def me(self) -> MeRequest:
		from .me import MeRequest
		return MeRequest(self.request_adapter, self.path_parameters)

	@property
	def privacy(self) -> PrivacyRequest:
		from .privacy import PrivacyRequest
		return PrivacyRequest(self.request_adapter, self.path_parameters)

	@property
	def devices_with_deviceid(self) -> DevicesWithDeviceIdRequest:
		from .devices_with_deviceid import DevicesWithDeviceIdRequest
		return DevicesWithDeviceIdRequest(self.request_adapter, self.path_parameters)

	@property
	def allowed_data_locations(self) -> AllowedDataLocationsRequest:
		from .allowed_data_locations import AllowedDataLocationsRequest
		return AllowedDataLocationsRequest(self.request_adapter, self.path_parameters)

	@property
	def oauth2_permission_grants(self) -> Oauth2PermissionGrantsRequest:
		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_role_assignments(self) -> PrivilegedRoleAssignmentsRequest:
		from .privileged_role_assignments import PrivilegedRoleAssignmentsRequest
		return PrivilegedRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grants(self) -> PermissionGrantsRequest:
		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def storage(self) -> StorageRequest:
		from .storage import StorageRequest
		return StorageRequest(self.request_adapter, self.path_parameters)

	@property
	def identity(self) -> IdentityRequest:
		from .identity import IdentityRequest
		return IdentityRequest(self.request_adapter, self.path_parameters)

	@property
	def solutions(self) -> SolutionsRequest:
		from .solutions import SolutionsRequest
		return SolutionsRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_objects(self) -> DirectoryObjectsRequest:
		from .directory_objects import DirectoryObjectsRequest
		return DirectoryObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def organization(self) -> OrganizationRequest:
		from .organization import OrganizationRequest
		return OrganizationRequest(self.request_adapter, self.path_parameters)

	@property
	def business_flow_templates(self) -> BusinessFlowTemplatesRequest:
		from .business_flow_templates import BusinessFlowTemplatesRequest
		return BusinessFlowTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def app(self) -> AppRequest:
		from .app import AppRequest
		return AppRequest(self.request_adapter, self.path_parameters)

	@property
	def users_with_userprincipalname(self) -> UsersWithUserPrincipalNameRequest:
		from .users_with_userprincipalname import UsersWithUserPrincipalNameRequest
		return UsersWithUserPrincipalNameRequest(self.request_adapter, self.path_parameters)

	@property
	def role_management(self) -> RoleManagementRequest:
		from .role_management import RoleManagementRequest
		return RoleManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def payload_response(self) -> PayloadResponseRequest:
		from .payload_response import PayloadResponseRequest
		return PayloadResponseRequest(self.request_adapter, self.path_parameters)

	@property
	def functions(self) -> FunctionsRequest:
		from .functions import FunctionsRequest
		return FunctionsRequest(self.request_adapter, self.path_parameters)

	@property
	def message_events(self) -> MessageEventsRequest:
		from .message_events import MessageEventsRequest
		return MessageEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def subscribed_skus(self) -> SubscribedSkusRequest:
		from .subscribed_skus import SubscribedSkusRequest
		return SubscribedSkusRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_role_assignment_requests(self) -> PrivilegedRoleAssignmentRequestsRequest:
		from .privileged_role_assignment_requests import PrivilegedRoleAssignmentRequestsRequest
		return PrivilegedRoleAssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_lifecycle_policies(self) -> GroupLifecyclePoliciesRequest:
		from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
		return GroupLifecyclePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_role_assignments(self) -> GovernanceRoleAssignmentsRequest:
		from .governance_role_assignments import GovernanceRoleAssignmentsRequest
		return GovernanceRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def network(self) -> NetworkRequest:
		from .network import NetworkRequest
		return NetworkRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_protection(self) -> IdentityProtectionRequest:
		from .identity_protection import IdentityProtectionRequest
		return IdentityProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def employee_experience(self) -> EmployeeExperienceRequest:
		from .employee_experience import EmployeeExperienceRequest
		return EmployeeExperienceRequest(self.request_adapter, self.path_parameters)

	@property
	def team_template_definition(self) -> TeamTemplateDefinitionRequest:
		from .team_template_definition import TeamTemplateDefinitionRequest
		return TeamTemplateDefinitionRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_roles(self) -> DirectoryRolesRequest:
		from .directory_roles import DirectoryRolesRequest
		return DirectoryRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def directory(self) -> DirectoryRequest:
		from .directory import DirectoryRequest
		return DirectoryRequest(self.request_adapter, self.path_parameters)

	@property
	def message_recipients(self) -> MessageRecipientsRequest:
		from .message_recipients import MessageRecipientsRequest
		return MessageRecipientsRequest(self.request_adapter, self.path_parameters)

	@property
	def print(self) -> PrintRequest:
		from .print import PrintRequest
		return PrintRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_roles(self) -> PrivilegedRolesRequest:
		from .privileged_roles import PrivilegedRolesRequest
		return PrivilegedRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def programs(self) -> ProgramsRequest:
		from .programs import ProgramsRequest
		return ProgramsRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_governance(self) -> IdentityGovernanceRequest:
		from .identity_governance import IdentityGovernanceRequest
		return IdentityGovernanceRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance(self) -> ComplianceRequest:
		from .compliance import ComplianceRequest
		return ComplianceRequest(self.request_adapter, self.path_parameters)

	@property
	def groups(self) -> GroupsRequest:
		from .groups import GroupsRequest
		return GroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def places_with_placeid(self) -> PlacesWithPlaceIdRequest:
		from .places_with_placeid import PlacesWithPlaceIdRequest
		return PlacesWithPlaceIdRequest(self.request_adapter, self.path_parameters)

	@property
	def governance_role_settings(self) -> GovernanceRoleSettingsRequest:
		from .governance_role_settings import GovernanceRoleSettingsRequest
		return GovernanceRoleSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_app_management(self) -> DeviceAppManagementRequest:
		from .device_app_management import DeviceAppManagementRequest
		return DeviceAppManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_role_templates(self) -> DirectoryRoleTemplatesRequest:
		from .directory_role_templates import DirectoryRoleTemplatesRequest
		return DirectoryRoleTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def domain_dns_records(self) -> DomainDnsRecordsRequest:
		from .domain_dns_records import DomainDnsRecordsRequest
		return DomainDnsRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_logs(self) -> AuditLogsRequest:
		from .audit_logs import AuditLogsRequest
		return AuditLogsRequest(self.request_adapter, self.path_parameters)

	@property
	def users(self) -> UsersRequest:
		from .users import UsersRequest
		return UsersRequest(self.request_adapter, self.path_parameters)

	@property
	def applications(self) -> ApplicationsRequest:
		from .applications import ApplicationsRequest
		return ApplicationsRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_based_auth_configuration(self) -> CertificateBasedAuthConfigurationRequest:
		from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
		return CertificateBasedAuthConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def domains(self) -> DomainsRequest:
		from .domains import DomainsRequest
		return DomainsRequest(self.request_adapter, self.path_parameters)


