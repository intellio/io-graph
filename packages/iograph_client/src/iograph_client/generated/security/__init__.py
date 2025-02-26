# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .trigger_types import TriggerTypesRequest
	from .triggers import TriggersRequest
	from .threat_intelligence import ThreatIntelligenceRequest
	from .subject_rights_requests import SubjectRightsRequestsRequest
	from .secure_scores import SecureScoresRequest
	from .secure_score_control_profiles import SecureScoreControlProfilesRequest
	from .security_run_hunting_query import SecurityRunHuntingQueryRequest
	from .labels import LabelsRequest
	from .incidents import IncidentsRequest
	from .identities import IdentitiesRequest
	from .cases import CasesRequest
	from .attack_simulation import AttackSimulationRequest
	from .alerts_v2 import Alerts_v2Request
	from .alerts import AlertsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security import Security


class SecurityRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security"
		self.path_parameters: dict[str, Any] = path_parameters

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
	def cases(self,
	) -> CasesRequest:
		from .cases import CasesRequest
		return CasesRequest(self.request_adapter, self.path_parameters)

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
	def triggers(self,
	) -> TriggersRequest:
		from .triggers import TriggersRequest
		return TriggersRequest(self.request_adapter, self.path_parameters)

	@property
	def trigger_types(self,
	) -> TriggerTypesRequest:
		from .trigger_types import TriggerTypesRequest
		return TriggerTypesRequest(self.request_adapter, self.path_parameters)

