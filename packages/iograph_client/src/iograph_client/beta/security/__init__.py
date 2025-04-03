# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_security_profiles import UserSecurityProfilesRequest
	from .trigger_types import TriggerTypesRequest
	from .triggers import TriggersRequest
	from .ti_indicators import TiIndicatorsRequest
	from .threat_submission import ThreatSubmissionRequest
	from .threat_intelligence import ThreatIntelligenceRequest
	from .subject_rights_requests import SubjectRightsRequestsRequest
	from .security_actions import SecurityActionsRequest
	from .secure_scores import SecureScoresRequest
	from .secure_score_control_profiles import SecureScoreControlProfilesRequest
	from .rules import RulesRequest
	from .provider_tenant_settings import ProviderTenantSettingsRequest
	from .partner import PartnerRequest
	from .security_run_hunting_query import SecurityRunHuntingQueryRequest
	from .labels import LabelsRequest
	from .ip_security_profiles import IpSecurityProfilesRequest
	from .information_protection import InformationProtectionRequest
	from .incidents import IncidentsRequest
	from .identities import IdentitiesRequest
	from .host_security_profiles import HostSecurityProfilesRequest
	from .file_security_profiles import FileSecurityProfilesRequest
	from .domain_security_profiles import DomainSecurityProfilesRequest
	from .data_discovery import DataDiscoveryRequest
	from .collaboration import CollaborationRequest
	from .cloud_app_security_profiles import CloudAppSecurityProfilesRequest
	from .cases import CasesRequest
	from .audit_log import AuditLogRequest
	from .attack_simulation import AttackSimulationRequest
	from .alerts_v2 import Alerts_v2Request
	from .alerts import AlertsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security import Security


class SecurityRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Security:
		"""
		Get security
		
		"""
		tags = ['security.security']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, Security, error_mapping)

	async def patch(
		self,
		body: Security,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Security:
		"""
		Update security
		
		"""
		tags = ['security.security']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Security, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SecurityRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecurityRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecurityRequest(self.request_adapter, self.path_parameters)

	@property
	def alerts(self,
	) -> AlertsRequest:
		from .alerts import AlertsRequest
		return AlertsRequest(self.request_adapter, self.path_parameters)

	@property
	def alerts_v2(self,
	) -> Alerts_v2Request:
		from .alerts_v2 import Alerts_v2Request
		return Alerts_v2Request(self.request_adapter, self.path_parameters)

	@property
	def attack_simulation(self,
	) -> AttackSimulationRequest:
		from .attack_simulation import AttackSimulationRequest
		return AttackSimulationRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_log(self,
	) -> AuditLogRequest:
		from .audit_log import AuditLogRequest
		return AuditLogRequest(self.request_adapter, self.path_parameters)

	@property
	def cases(self,
	) -> CasesRequest:
		from .cases import CasesRequest
		return CasesRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_app_security_profiles(self,
	) -> CloudAppSecurityProfilesRequest:
		from .cloud_app_security_profiles import CloudAppSecurityProfilesRequest
		return CloudAppSecurityProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def collaboration(self,
	) -> CollaborationRequest:
		from .collaboration import CollaborationRequest
		return CollaborationRequest(self.request_adapter, self.path_parameters)

	@property
	def data_discovery(self,
	) -> DataDiscoveryRequest:
		from .data_discovery import DataDiscoveryRequest
		return DataDiscoveryRequest(self.request_adapter, self.path_parameters)

	@property
	def domain_security_profiles(self,
	) -> DomainSecurityProfilesRequest:
		from .domain_security_profiles import DomainSecurityProfilesRequest
		return DomainSecurityProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def file_security_profiles(self,
	) -> FileSecurityProfilesRequest:
		from .file_security_profiles import FileSecurityProfilesRequest
		return FileSecurityProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def host_security_profiles(self,
	) -> HostSecurityProfilesRequest:
		from .host_security_profiles import HostSecurityProfilesRequest
		return HostSecurityProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def identities(self,
	) -> IdentitiesRequest:
		from .identities import IdentitiesRequest
		return IdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def incidents(self,
	) -> IncidentsRequest:
		from .incidents import IncidentsRequest
		return IncidentsRequest(self.request_adapter, self.path_parameters)

	@property
	def information_protection(self,
	) -> InformationProtectionRequest:
		from .information_protection import InformationProtectionRequest
		return InformationProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def ip_security_profiles(self,
	) -> IpSecurityProfilesRequest:
		from .ip_security_profiles import IpSecurityProfilesRequest
		return IpSecurityProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def labels(self,
	) -> LabelsRequest:
		from .labels import LabelsRequest
		return LabelsRequest(self.request_adapter, self.path_parameters)

	@property
	def security_run_hunting_query(self,
	) -> SecurityRunHuntingQueryRequest:
		from .security_run_hunting_query import SecurityRunHuntingQueryRequest
		return SecurityRunHuntingQueryRequest(self.request_adapter, self.path_parameters)

	@property
	def partner(self,
	) -> PartnerRequest:
		from .partner import PartnerRequest
		return PartnerRequest(self.request_adapter, self.path_parameters)

	@property
	def provider_tenant_settings(self,
	) -> ProviderTenantSettingsRequest:
		from .provider_tenant_settings import ProviderTenantSettingsRequest
		return ProviderTenantSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def rules(self,
	) -> RulesRequest:
		from .rules import RulesRequest
		return RulesRequest(self.request_adapter, self.path_parameters)

	@property
	def secure_score_control_profiles(self,
	) -> SecureScoreControlProfilesRequest:
		from .secure_score_control_profiles import SecureScoreControlProfilesRequest
		return SecureScoreControlProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def secure_scores(self,
	) -> SecureScoresRequest:
		from .secure_scores import SecureScoresRequest
		return SecureScoresRequest(self.request_adapter, self.path_parameters)

	@property
	def security_actions(self,
	) -> SecurityActionsRequest:
		from .security_actions import SecurityActionsRequest
		return SecurityActionsRequest(self.request_adapter, self.path_parameters)

	@property
	def subject_rights_requests(self,
	) -> SubjectRightsRequestsRequest:
		from .subject_rights_requests import SubjectRightsRequestsRequest
		return SubjectRightsRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def threat_intelligence(self,
	) -> ThreatIntelligenceRequest:
		from .threat_intelligence import ThreatIntelligenceRequest
		return ThreatIntelligenceRequest(self.request_adapter, self.path_parameters)

	@property
	def threat_submission(self,
	) -> ThreatSubmissionRequest:
		from .threat_submission import ThreatSubmissionRequest
		return ThreatSubmissionRequest(self.request_adapter, self.path_parameters)

	@property
	def ti_indicators(self,
	) -> TiIndicatorsRequest:
		from .ti_indicators import TiIndicatorsRequest
		return TiIndicatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def triggers(self,
	) -> TriggersRequest:
		from .triggers import TriggersRequest
		return TriggersRequest(self.request_adapter, self.path_parameters)

	@property
	def trigger_types(self,
	) -> TriggerTypesRequest:
		from .trigger_types import TriggerTypesRequest
		return TriggerTypesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_security_profiles(self,
	) -> UserSecurityProfilesRequest:
		from .user_security_profiles import UserSecurityProfilesRequest
		return UserSecurityProfilesRequest(self.request_adapter, self.path_parameters)

