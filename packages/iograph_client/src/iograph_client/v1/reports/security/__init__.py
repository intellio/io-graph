# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_attack_simulation_training_user_coverage import GetAttackSimulationTrainingUserCoverageRequest
	from .get_attack_simulation_simulation_user_coverage import GetAttackSimulationSimulationUserCoverageRequest
	from .get_attack_simulation_repeat_offenders import GetAttackSimulationRepeatOffendersRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_reports_root import SecurityReportsRoot
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SecurityRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/security", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityReportsRoot:
		"""
		Get security from reports
		Represents an abstract type that contains resources for attack simulation and training reports.
		"""
		tags = ['reports.securityReportsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityReportsRoot, error_mapping)

	async def patch(
		self,
		body: SecurityReportsRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityReportsRoot:
		"""
		Update the navigation property security in reports
		
		"""
		tags = ['reports.securityReportsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityReportsRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property security for reports
		
		"""
		tags = ['reports.securityReportsRoot']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

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
	def get_attack_simulation_repeat_offenders(self,
	) -> GetAttackSimulationRepeatOffendersRequest:
		from .get_attack_simulation_repeat_offenders import GetAttackSimulationRepeatOffendersRequest
		return GetAttackSimulationRepeatOffendersRequest(self.request_adapter, self.path_parameters)

	@property
	def get_attack_simulation_simulation_user_coverage(self,
	) -> GetAttackSimulationSimulationUserCoverageRequest:
		from .get_attack_simulation_simulation_user_coverage import GetAttackSimulationSimulationUserCoverageRequest
		return GetAttackSimulationSimulationUserCoverageRequest(self.request_adapter, self.path_parameters)

	@property
	def get_attack_simulation_training_user_coverage(self,
	) -> GetAttackSimulationTrainingUserCoverageRequest:
		from .get_attack_simulation_training_user_coverage import GetAttackSimulationTrainingUserCoverageRequest
		return GetAttackSimulationTrainingUserCoverageRequest(self.request_adapter, self.path_parameters)

