# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_my_role_tenant_id import ByMyRoleTenantIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_my_role_collection_response import ManagedTenantsMyRoleCollectionResponse
from iograph_models.beta.managed_tenants_my_role import ManagedTenantsMyRole
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MyRolesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/myRoles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedTenantsMyRoleCollectionResponse:
		"""
		List myRoles
		Get the roles that a signed-in user has through a delegated relationship across managed tenants. For information on the types of delegated relationships between a Managed Service Provider (MSP) who uses Microsoft 365 Lighthouse, and their business customers with Microsoft 365 Business Premium tenants, see the following articles on the Partner Center:
- Delegated administration privileges (DAP)
- Granular delegated admin privileges (GDAP)
		Find more info here: https://learn.microsoft.com/graph/api/managedtenants-managedtenant-list-myroles?view=graph-rest-beta
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsMyRoleCollectionResponse, error_mapping)

	async def post(
		self,
		body: ManagedTenantsMyRole,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsMyRole:
		"""
		Create new navigation property to myRoles for tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsMyRole, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MyRolesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MyRolesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MyRolesRequest(self.request_adapter, self.path_parameters)

	def by_my_role_tenant_id(self,
		myRole_tenantId: str,
	) -> ByMyRoleTenantIdRequest:
		if myRole_tenantId is None:
			raise TypeError("myRole_tenantId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["myRole%2DtenantId"] =  myRole_tenantId

		from .by_my_role_tenant_id import ByMyRoleTenantIdRequest
		return ByMyRoleTenantIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

