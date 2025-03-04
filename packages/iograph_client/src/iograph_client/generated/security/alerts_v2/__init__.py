# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_alert_id import ByAlertIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.security_alert import SecurityAlert
from iograph_models.models.security_alert_collection_response import SecurityAlertCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class Alerts_v2Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/alerts_v2", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityAlertCollectionResponse:
		"""
		List alerts_v2
		Get a list of alert resources created to track suspicious activities in an organization. This operation lets you filter and sort through alerts to create an informed cyber security response. It exposes a collection of alerts that were flagged in your network, within the time range you specified in your environment retention policy. The most recent alerts are displayed at the top of the list.
		Find more info here: https://learn.microsoft.com/graph/api/security-list-alerts_v2?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityAlertCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityAlert,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityAlert:
		"""
		Create new navigation property to alerts_v2 for security
		
		"""
		tags = ['security.alert']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, SecurityAlert, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> Alerts_v2Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: Alerts_v2Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return Alerts_v2Request(self.request_adapter, self.path_parameters)

	def by_alert_id(self,
		alert_id: str,
	) -> ByAlertIdRequest:
		if alert_id is None:
			raise TypeError("alert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["alert%2Did"] =  alert_id

		from .by_alert_id import ByAlertIdRequest
		return ByAlertIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

