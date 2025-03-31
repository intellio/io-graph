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
	from .update_policies import UpdatePoliciesRequest
	from .updatable_assets import UpdatableAssetsRequest
	from .resource_connections import ResourceConnectionsRequest
	from .products import ProductsRequest
	from .deployments import DeploymentsRequest
	from .deployment_audiences import DeploymentAudiencesRequest
	from .catalog import CatalogRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.admin_windows_updates import AdminWindowsUpdates
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UpdatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AdminWindowsUpdates:
		"""
		Get updates from admin
		Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, AdminWindowsUpdates, error_mapping)

	async def patch(
		self,
		body: AdminWindowsUpdates,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AdminWindowsUpdates:
		"""
		Update the navigation property updates in admin
		
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, AdminWindowsUpdates, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property updates for admin
		
		"""
		tags = ['admin.adminWindows']
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



	def with_url(self, raw_url: str) -> UpdatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UpdatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UpdatesRequest(self.request_adapter, self.path_parameters)

	@property
	def catalog(self,
	) -> CatalogRequest:
		from .catalog import CatalogRequest
		return CatalogRequest(self.request_adapter, self.path_parameters)

	@property
	def deployment_audiences(self,
	) -> DeploymentAudiencesRequest:
		from .deployment_audiences import DeploymentAudiencesRequest
		return DeploymentAudiencesRequest(self.request_adapter, self.path_parameters)

	@property
	def deployments(self,
	) -> DeploymentsRequest:
		from .deployments import DeploymentsRequest
		return DeploymentsRequest(self.request_adapter, self.path_parameters)

	@property
	def products(self,
	) -> ProductsRequest:
		from .products import ProductsRequest
		return ProductsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_connections(self,
	) -> ResourceConnectionsRequest:
		from .resource_connections import ResourceConnectionsRequest
		return ResourceConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def updatable_assets(self,
	) -> UpdatableAssetsRequest:
		from .updatable_assets import UpdatableAssetsRequest
		return UpdatableAssetsRequest(self.request_adapter, self.path_parameters)

	@property
	def update_policies(self,
	) -> UpdatePoliciesRequest:
		from .update_policies import UpdatePoliciesRequest
		return UpdatePoliciesRequest(self.request_adapter, self.path_parameters)

