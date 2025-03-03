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
	from .by_access_package_resource_role_id1 import ByAccessPackageResourceRoleId1Request
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.access_package_resource_role import AccessPackageResourceRole
from iograph_models.models.access_package_resource_role_collection_response import AccessPackageResourceRoleCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class RolesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}/resourceRoles/{accessPackageResourceRole%2Did}/resource/roles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageResourceRoleCollectionResponse:
		"""
		Get roles from identityGovernance
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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceRoleCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessPackageResourceRole,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageResourceRole:
		"""
		Create new navigation property to roles for identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceRole, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RolesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RolesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RolesRequest(self.request_adapter, self.path_parameters)

	def by_access_package_resource_role_id1(self,
		accessPackageCatalog_id: str,
		accessPackageResourceRole_id: str,
		accessPackageResourceRole_id1: str,
	) -> ByAccessPackageResourceRoleId1Request:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if accessPackageResourceRole_id is None:
			raise TypeError("accessPackageResourceRole_id cannot be null.")
		if accessPackageResourceRole_id1 is None:
			raise TypeError("accessPackageResourceRole_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["accessPackageResourceRole%2Did"] =  accessPackageResourceRole_id
		path_parameters["accessPackageResourceRole%2Did1"] =  accessPackageResourceRole_id1

		from .by_access_package_resource_role_id1 import ByAccessPackageResourceRoleId1Request
		return ByAccessPackageResourceRoleId1Request(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

