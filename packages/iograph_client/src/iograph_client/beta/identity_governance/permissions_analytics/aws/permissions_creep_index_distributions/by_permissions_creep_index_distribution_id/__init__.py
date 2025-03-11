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
	from .authorization_system import AuthorizationSystemRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.permissions_creep_index_distribution import PermissionsCreepIndexDistribution
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPermissionsCreepIndexDistributionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/permissionsAnalytics/aws/permissionsCreepIndexDistributions/{permissionsCreepIndexDistribution%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionsCreepIndexDistribution:
		"""
		Get permissionsCreepIndexDistributions from identityGovernance
		Represents the Permissions Creep Index (PCI) for the authorization system. PCI distribution chart shows the classification of human and nonhuman identities based on the PCI score in three buckets (low, medium, high).
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
		return await self.request_adapter.send_async(request_info, PermissionsCreepIndexDistribution, error_mapping)

	async def patch(
		self,
		body: PermissionsCreepIndexDistribution,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PermissionsCreepIndexDistribution:
		"""
		Update the navigation property permissionsCreepIndexDistributions in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PermissionsCreepIndexDistribution, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property permissionsCreepIndexDistributions for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByPermissionsCreepIndexDistributionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPermissionsCreepIndexDistributionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPermissionsCreepIndexDistributionIdRequest(self.request_adapter, self.path_parameters)

	def authorization_system(self,
		permissionsCreepIndexDistribution_id: str,
	) -> AuthorizationSystemRequest:
		if permissionsCreepIndexDistribution_id is None:
			raise TypeError("permissionsCreepIndexDistribution_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["permissionsCreepIndexDistribution%2Did"] =  permissionsCreepIndexDistribution_id

		from .authorization_system import AuthorizationSystemRequest
		return AuthorizationSystemRequest(self.request_adapter, path_parameters)

