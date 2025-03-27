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
	from .permissions_creep_index_distributions import PermissionsCreepIndexDistributionsRequest
	from .findings import FindingsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.permissions_analytics import PermissionsAnalytics


class AwsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/permissionsAnalytics/aws", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionsAnalytics:
		"""
		Get aws from identityGovernance
		AWS permissions analytics findings.
		"""
		tags = ['identityGovernance.permissionsAnalyticsAggregation']

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
		return await self.request_adapter.send_async(request_info, PermissionsAnalytics, error_mapping)

	async def patch(
		self,
		body: PermissionsAnalytics,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PermissionsAnalytics:
		"""
		Update the navigation property aws in identityGovernance
		
		"""
		tags = ['identityGovernance.permissionsAnalyticsAggregation']

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
		return await self.request_adapter.send_async(request_info, PermissionsAnalytics, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property aws for identityGovernance
		
		"""
		tags = ['identityGovernance.permissionsAnalyticsAggregation']
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



	def with_url(self, raw_url: str) -> AwsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AwsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AwsRequest(self.request_adapter, self.path_parameters)

	@property
	def findings(self,
	) -> FindingsRequest:
		from .findings import FindingsRequest
		return FindingsRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions_creep_index_distributions(self,
	) -> PermissionsCreepIndexDistributionsRequest:
		from .permissions_creep_index_distributions import PermissionsCreepIndexDistributionsRequest
		return PermissionsCreepIndexDistributionsRequest(self.request_adapter, self.path_parameters)

