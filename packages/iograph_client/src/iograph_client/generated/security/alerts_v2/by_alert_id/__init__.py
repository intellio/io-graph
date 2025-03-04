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
	from .comments import CommentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.security_alert import SecurityAlert
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAlertIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/alerts_v2/{alert%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityAlert:
		"""
		Get alert
		Get the properties and relationships of an alert object.
		Find more info here: https://learn.microsoft.com/graph/api/security-alert-get?view=graph-rest-1.0
		"""
		tags = ['security.alert']

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
		return await self.request_adapter.send_async(request_info, SecurityAlert, error_mapping)

	async def patch(
		self,
		body: SecurityAlert,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityAlert:
		"""
		Update alert
		Update the properties of an alert object in an organization based on the specified alert id property.
		Find more info here: https://learn.microsoft.com/graph/api/security-alert-update?view=graph-rest-1.0
		"""
		tags = ['security.alert']

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
		return await self.request_adapter.send_async(request_info, SecurityAlert, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property alerts_v2 for security
		
		"""
		tags = ['security.alert']
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



	def with_url(self, raw_url: str) -> ByAlertIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAlertIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAlertIdRequest(self.request_adapter, self.path_parameters)

	def comments(self,
		alert_id: str,
	) -> CommentsRequest:
		if alert_id is None:
			raise TypeError("alert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["alert%2Did"] =  alert_id

		from .comments import CommentsRequest
		return CommentsRequest(self.request_adapter, path_parameters)

