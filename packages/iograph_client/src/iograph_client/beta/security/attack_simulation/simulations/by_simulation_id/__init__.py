# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .payload import PayloadRequest
	from .login_page import LoginPageRequest
	from .landing_page import LandingPageRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.simulation import Simulation


class BySimulationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/attackSimulation/simulations/{simulation%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Simulation:
		"""
		Get simulation
		Get an attack simulation campaign for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/simulation-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Simulation, error_mapping)

	async def patch(
		self,
		body: Simulation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Simulation:
		"""
		Update simulation
		Update an attack simulation campaign for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/simulation-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Simulation, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete simulation
		Delete an attack simulation campaign for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/simulation-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> BySimulationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySimulationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySimulationIdRequest(self.request_adapter, self.path_parameters)

	def landing_page(self,
		simulation_id: str,
	) -> LandingPageRequest:
		if simulation_id is None:
			raise TypeError("simulation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["simulation%2Did"] =  simulation_id

		from .landing_page import LandingPageRequest
		return LandingPageRequest(self.request_adapter, path_parameters)

	def login_page(self,
		simulation_id: str,
	) -> LoginPageRequest:
		if simulation_id is None:
			raise TypeError("simulation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["simulation%2Did"] =  simulation_id

		from .login_page import LoginPageRequest
		return LoginPageRequest(self.request_adapter, path_parameters)

	def payload(self,
		simulation_id: str,
	) -> PayloadRequest:
		if simulation_id is None:
			raise TypeError("simulation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["simulation%2Did"] =  simulation_id

		from .payload import PayloadRequest
		return PayloadRequest(self.request_adapter, path_parameters)

