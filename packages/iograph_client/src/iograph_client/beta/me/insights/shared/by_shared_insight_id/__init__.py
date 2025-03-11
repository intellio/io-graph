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
	from .resource import ResourceRequest
	from .last_shared_method import LastSharedMethodRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.shared_insight import SharedInsight
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySharedInsightIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/insights/shared/{sharedInsight%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedInsight:
		"""
		Get shared from me
		Access this property from the derived type itemInsights.
		"""
		tags = ['me.itemInsights']

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
		return await self.request_adapter.send_async(request_info, SharedInsight, error_mapping)

	async def patch(
		self,
		body: SharedInsight,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedInsight:
		"""
		Update the navigation property shared in me
		
		"""
		tags = ['me.itemInsights']

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
		return await self.request_adapter.send_async(request_info, SharedInsight, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property shared for me
		
		"""
		tags = ['me.itemInsights']
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



	def with_url(self, raw_url: str) -> BySharedInsightIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySharedInsightIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySharedInsightIdRequest(self.request_adapter, self.path_parameters)

	def last_shared_method(self,
		sharedInsight_id: str,
	) -> LastSharedMethodRequest:
		if sharedInsight_id is None:
			raise TypeError("sharedInsight_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedInsight%2Did"] =  sharedInsight_id

		from .last_shared_method import LastSharedMethodRequest
		return LastSharedMethodRequest(self.request_adapter, path_parameters)

	def resource(self,
		sharedInsight_id: str,
	) -> ResourceRequest:
		if sharedInsight_id is None:
			raise TypeError("sharedInsight_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedInsight%2Did"] =  sharedInsight_id

		from .resource import ResourceRequest
		return ResourceRequest(self.request_adapter, path_parameters)

