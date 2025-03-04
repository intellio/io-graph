# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .comments import CommentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.security_alert import SecurityAlert
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAlertIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/incidents/{incident%2Did}/alerts/{alert%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityAlert:
		"""
		Get alerts from security
		The list of related alerts. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, SecurityAlert, error_mapping)

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
		incident_id: str,
		alert_id: str,
	) -> CommentsRequest:
		if incident_id is None:
			raise TypeError("incident_id cannot be null.")
		if alert_id is None:
			raise TypeError("alert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["incident%2Did"] =  incident_id
		path_parameters["alert%2Did"] =  alert_id

		from .comments import CommentsRequest
		return CommentsRequest(self.request_adapter, path_parameters)

