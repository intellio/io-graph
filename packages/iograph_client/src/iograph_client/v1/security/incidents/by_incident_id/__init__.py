# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .alerts import AlertsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_incident import SecurityIncident
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByIncidentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/incidents/{incident%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityIncident:
		"""
		Get incident
		Retrieve the properties and relationships of an incident object. Attacks are typically inflicted on different types of entities, such as devices, users, and mailboxes, resulting in multiple alert objects. Microsoft 365 Defender correlates alerts with the same attack techniques or the same attacker into an incident.
		Find more info here: https://learn.microsoft.com/graph/api/security-incident-get?view=graph-rest-1.0
		"""
		tags = ['security.incident']

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
		return await self.request_adapter.send_async(request_info, SecurityIncident, error_mapping)

	async def patch(
		self,
		body: SecurityIncident,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityIncident:
		"""
		Update incident
		Update the properties of an incident object.
		Find more info here: https://learn.microsoft.com/graph/api/security-incident-update?view=graph-rest-1.0
		"""
		tags = ['security.incident']

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
		return await self.request_adapter.send_async(request_info, SecurityIncident, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property incidents for security
		
		"""
		tags = ['security.incident']
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



	def with_url(self, raw_url: str) -> ByIncidentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByIncidentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByIncidentIdRequest(self.request_adapter, self.path_parameters)

	def alerts(self,
		incident_id: str,
	) -> AlertsRequest:
		if incident_id is None:
			raise TypeError("incident_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["incident%2Did"] =  incident_id

		from .alerts import AlertsRequest
		return AlertsRequest(self.request_adapter, path_parameters)

