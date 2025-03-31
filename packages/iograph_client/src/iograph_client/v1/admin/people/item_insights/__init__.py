# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.insights_settings import InsightsSettings
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ItemInsightsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/people/itemInsights", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InsightsSettings:
		"""
		List itemInsights
		Get the properties of an insightsSettings object to display or return item insights in an organization. To learn how to customize the privacy of item insights in an organization, see Customize item insights privacy in Microsoft Graph.
		Find more info here: https://learn.microsoft.com/graph/api/peopleadminsettings-list-iteminsights?view=graph-rest-1.0
		"""
		tags = ['admin.peopleAdminSettings']

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
		return await self.request_adapter.send_async(request_info, InsightsSettings, error_mapping)

	async def patch(
		self,
		body: InsightsSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InsightsSettings:
		"""
		Update insightsSettings
		Update privacy settings to display or return the specified type of insights in an organization. Currently, itemInsights is the only supported type of settings. To learn more about customizing insights privacy for your organization, see Customize item insights privacy in Microsoft Graph.
		Find more info here: https://learn.microsoft.com/graph/api/insightssettings-update?view=graph-rest-1.0
		"""
		tags = ['admin.peopleAdminSettings']

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
		return await self.request_adapter.send_async(request_info, InsightsSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property itemInsights for admin
		
		"""
		tags = ['admin.peopleAdminSettings']
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



	def with_url(self, raw_url: str) -> ItemInsightsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemInsightsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemInsightsRequest(self.request_adapter, self.path_parameters)

