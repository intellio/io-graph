# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .scopes import ScopesRequest
	from .roles import RolesRequest
	from .environment import EnvironmentRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.access_package_resource import AccessPackageResource
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessPackageResourceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}/resources/{accessPackageResource%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageResource:
		"""
		Get resources from identityGovernance
		Access package resources in this catalog.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageResource, error_mapping)

	async def patch(
		self,
		body: AccessPackageResource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageResource:
		"""
		Update the navigation property resources in identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageResource, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property resources for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']
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



	def with_url(self, raw_url: str) -> ByAccessPackageResourceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageResourceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageResourceIdRequest(self.request_adapter, self.path_parameters)

	def environment(self,
		accessPackageCatalog_id: str,
		accessPackageResource_id: str,
	) -> EnvironmentRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResource_id is None:
			raise TypeError("accessPackageResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResource%2Did"] =  accessPackageResource_id

		from .environment import EnvironmentRequest
		return EnvironmentRequest(self.request_adapter, path_parameters)

	def roles(self,
		accessPackageCatalog_id: str,
		accessPackageResource_id: str,
	) -> RolesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResource_id is None:
			raise TypeError("accessPackageResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResource%2Did"] =  accessPackageResource_id

		from .roles import RolesRequest
		return RolesRequest(self.request_adapter, path_parameters)

	def scopes(self,
		accessPackageCatalog_id: str,
		accessPackageResource_id: str,
	) -> ScopesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResource_id is None:
			raise TypeError("accessPackageResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResource%2Did"] =  accessPackageResource_id

		from .scopes import ScopesRequest
		return ScopesRequest(self.request_adapter, path_parameters)

