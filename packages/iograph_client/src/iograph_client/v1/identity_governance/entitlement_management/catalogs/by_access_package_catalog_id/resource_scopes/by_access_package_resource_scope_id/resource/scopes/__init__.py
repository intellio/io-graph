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
	from .count import CountRequest
	from .by_access_package_resource_scope_id1 import ByAccessPackageResourceScopeId1Request
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.access_package_resource_scope import AccessPackageResourceScope
from iograph_models.v1.access_package_resource_scope_collection_response import AccessPackageResourceScopeCollectionResponse


class ScopesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}/resourceScopes/{accessPackageResourceScope%2Did}/resource/scopes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageResourceScopeCollectionResponse:
		"""
		Get scopes from identityGovernance
		Read-only. Nullable. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceScopeCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessPackageResourceScope,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageResourceScope:
		"""
		Create new navigation property to scopes for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceScope, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ScopesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ScopesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ScopesRequest(self.request_adapter, self.path_parameters)

	def by_access_package_resource_scope_id1(self,
		accessPackageCatalog_id: str,
		accessPackageResourceScope_id: str,
		accessPackageResourceScope_id1: str,
	) -> ByAccessPackageResourceScopeId1Request:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResourceScope_id is None:
			raise TypeError("accessPackageResourceScope_id cannot be null.")
		if accessPackageResourceScope_id1 is None:
			raise TypeError("accessPackageResourceScope_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResourceScope%2Did"] =  accessPackageResourceScope_id
		path_parameters["accessPackageResourceScope%2Did1"] =  accessPackageResourceScope_id1

		from .by_access_package_resource_scope_id1 import ByAccessPackageResourceScopeId1Request
		return ByAccessPackageResourceScopeId1Request(self.request_adapter, path_parameters)

	def count(self,
		accessPackageCatalog_id: str,
		accessPackageResourceScope_id: str,
	) -> CountRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResourceScope_id is None:
			raise TypeError("accessPackageResourceScope_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResourceScope%2Did"] =  accessPackageResourceScope_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

