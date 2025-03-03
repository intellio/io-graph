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
	from .trainings import TrainingsRequest
	from .simulations import SimulationsRequest
	from .simulation_automations import SimulationAutomationsRequest
	from .payloads import PayloadsRequest
	from .operations import OperationsRequest
	from .login_pages import LoginPagesRequest
	from .landing_pages import LandingPagesRequest
	from .end_user_notifications import EndUserNotificationsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.attack_simulation_root import AttackSimulationRoot
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class AttackSimulationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/attackSimulation", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttackSimulationRoot:
		"""
		Get attackSimulation from security
		
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, AttackSimulationRoot, error_mapping)

	async def patch(
		self,
		body: AttackSimulationRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AttackSimulationRoot:
		"""
		Update the navigation property attackSimulation in security
		
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, AttackSimulationRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property attackSimulation for security
		
		"""
		tags = ['security.attackSimulationRoot']
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



	def with_url(self, raw_url: str) -> AttackSimulationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AttackSimulationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AttackSimulationRequest(self.request_adapter, self.path_parameters)

	@property
	def end_user_notifications(self,
	) -> EndUserNotificationsRequest:
		from .end_user_notifications import EndUserNotificationsRequest
		return EndUserNotificationsRequest(self.request_adapter, self.path_parameters)

	@property
	def landing_pages(self,
	) -> LandingPagesRequest:
		from .landing_pages import LandingPagesRequest
		return LandingPagesRequest(self.request_adapter, self.path_parameters)

	@property
	def login_pages(self,
	) -> LoginPagesRequest:
		from .login_pages import LoginPagesRequest
		return LoginPagesRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def payloads(self,
	) -> PayloadsRequest:
		from .payloads import PayloadsRequest
		return PayloadsRequest(self.request_adapter, self.path_parameters)

	@property
	def simulation_automations(self,
	) -> SimulationAutomationsRequest:
		from .simulation_automations import SimulationAutomationsRequest
		return SimulationAutomationsRequest(self.request_adapter, self.path_parameters)

	@property
	def simulations(self,
	) -> SimulationsRequest:
		from .simulations import SimulationsRequest
		return SimulationsRequest(self.request_adapter, self.path_parameters)

	@property
	def trainings(self,
	) -> TrainingsRequest:
		from .trainings import TrainingsRequest
		return TrainingsRequest(self.request_adapter, self.path_parameters)

