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
	from .resource_scopes import ResourceScopesRequest
	from .resources import ResourcesRequest
	from .resource_roles import ResourceRolesRequest
	from .custom_workflow_extensions import CustomWorkflowExtensionsRequest
	from .access_packages import AccessPackagesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.access_package_catalog import AccessPackageCatalog
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessPackageCatalogIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}", path_parameters)

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



	def with_url(self, raw_url: str) -> ByAccessPackageCatalogIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageCatalogIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageCatalogIdRequest(self.request_adapter, self.path_parameters)

	def access_packages(self,
		accessPackageCatalog_id: str,
	) -> AccessPackagesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_packages import AccessPackagesRequest
		return AccessPackagesRequest(self.request_adapter, path_parameters)

	def custom_workflow_extensions(self,
		accessPackageCatalog_id: str,
	) -> CustomWorkflowExtensionsRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .custom_workflow_extensions import CustomWorkflowExtensionsRequest
		return CustomWorkflowExtensionsRequest(self.request_adapter, path_parameters)

	def resource_roles(self,
		accessPackageCatalog_id: str,
	) -> ResourceRolesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .resource_roles import ResourceRolesRequest
		return ResourceRolesRequest(self.request_adapter, path_parameters)

	def resources(self,
		accessPackageCatalog_id: str,
	) -> ResourcesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, path_parameters)

	def resource_scopes(self,
		accessPackageCatalog_id: str,
	) -> ResourceScopesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .resource_scopes import ResourceScopesRequest
		return ResourceScopesRequest(self.request_adapter, path_parameters)

