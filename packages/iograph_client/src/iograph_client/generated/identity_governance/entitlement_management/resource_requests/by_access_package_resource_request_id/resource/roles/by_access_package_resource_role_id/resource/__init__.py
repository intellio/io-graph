# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .scopes import ScopesRequest
	from .environment import EnvironmentRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_package_resource import AccessPackageResource


class ResourceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/resourceRequests/{accessPackageResourceRequest%2Did}/resource/roles/{accessPackageResourceRole%2Did}/resource", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageResource:
		"""
		Get resource from identityGovernance
		
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
		Update the navigation property resource in identityGovernance
		
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
		Delete navigation property resource for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ResourceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResourceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResourceRequest(self.request_adapter, self.path_parameters)

	def environment(self,
		accessPackageResourceRequest_id: str,
		accessPackageResourceRole_id: str,
	) -> EnvironmentRequest:
		if accessPackageResourceRequest_id is None:
			raise TypeError("accessPackageResourceRequest_id cannot be null.")
		if accessPackageResourceRole_id is None:
			raise TypeError("accessPackageResourceRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageResourceRequest%2Did"] =  accessPackageResourceRequest_id
		path_parameters["accessPackageResourceRole%2Did"] =  accessPackageResourceRole_id

		from .environment import EnvironmentRequest
		return EnvironmentRequest(self.request_adapter, path_parameters)

	def scopes(self,
		accessPackageResourceRequest_id: str,
		accessPackageResourceRole_id: str,
	) -> ScopesRequest:
		if accessPackageResourceRequest_id is None:
			raise TypeError("accessPackageResourceRequest_id cannot be null.")
		if accessPackageResourceRole_id is None:
			raise TypeError("accessPackageResourceRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageResourceRequest%2Did"] =  accessPackageResourceRequest_id
		path_parameters["accessPackageResourceRole%2Did"] =  accessPackageResourceRole_id

		from .scopes import ScopesRequest
		return ScopesRequest(self.request_adapter, path_parameters)

