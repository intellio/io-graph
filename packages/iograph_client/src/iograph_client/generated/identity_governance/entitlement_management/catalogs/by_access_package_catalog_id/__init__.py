# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .resource_scopes import ResourceScopesRequest
	from .resources import ResourcesRequest
	from .resource_roles import ResourceRolesRequest
	from .custom_workflow_extensions import CustomWorkflowExtensionsRequest
	from .access_packages import AccessPackagesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_package_catalog import AccessPackageCatalog


class ByAccessPackageCatalogIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageCatalog:
		"""
		Get accessPackageCatalog
		Retrieve the properties and relationships of an accessPackageCatalog object.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)

	async def patch(
		self,
		body: AccessPackageCatalog,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageCatalog:
		"""
		Update accessPackageCatalog
		Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete accessPackageCatalog
		Delete an accessPackageCatalog.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-delete?view=graph-rest-1.0
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



	@property
	def access_packages(self,
	) -> AccessPackagesRequest:
		from .access_packages import AccessPackagesRequest
		return AccessPackagesRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_workflow_extensions(self,
	) -> CustomWorkflowExtensionsRequest:
		from .custom_workflow_extensions import CustomWorkflowExtensionsRequest
		return CustomWorkflowExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_roles(self,
	) -> ResourceRolesRequest:
		from .resource_roles import ResourceRolesRequest
		return ResourceRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def resources(self,
	) -> ResourcesRequest:
		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_scopes(self,
	) -> ResourceScopesRequest:
		from .resource_scopes import ResourceScopesRequest
		return ResourceScopesRequest(self.request_adapter, self.path_parameters)

