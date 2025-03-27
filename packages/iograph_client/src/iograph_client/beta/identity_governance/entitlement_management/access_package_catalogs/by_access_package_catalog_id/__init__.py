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
	from .custom_access_package_workflow_extensions import CustomAccessPackageWorkflowExtensionsRequest
	from .access_packages_with_uniquename import AccessPackagesWithUniqueNameRequest
	from .access_packages import AccessPackagesRequest
	from .access_package_resource_scopes import AccessPackageResourceScopesRequest
	from .access_package_resources import AccessPackageResourcesRequest
	from .access_package_resource_roles import AccessPackageResourceRolesRequest
	from .access_package_custom_workflow_extensions import AccessPackageCustomWorkflowExtensionsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_catalog import AccessPackageCatalog


class ByAccessPackageCatalogIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageCatalog:
		"""
		Get accessPackageCatalog
		Retrieve the properties and relationships of an accessPackageCatalog object.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-get?view=graph-rest-beta
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
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-update?view=graph-rest-beta
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
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-delete?view=graph-rest-beta
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

	def access_package_custom_workflow_extensions(self,
		accessPackageCatalog_id: str,
	) -> AccessPackageCustomWorkflowExtensionsRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_package_custom_workflow_extensions import AccessPackageCustomWorkflowExtensionsRequest
		return AccessPackageCustomWorkflowExtensionsRequest(self.request_adapter, path_parameters)

	def access_package_resource_roles(self,
		accessPackageCatalog_id: str,
	) -> AccessPackageResourceRolesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_package_resource_roles import AccessPackageResourceRolesRequest
		return AccessPackageResourceRolesRequest(self.request_adapter, path_parameters)

	def access_package_resources(self,
		accessPackageCatalog_id: str,
	) -> AccessPackageResourcesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_package_resources import AccessPackageResourcesRequest
		return AccessPackageResourcesRequest(self.request_adapter, path_parameters)

	def access_package_resource_scopes(self,
		accessPackageCatalog_id: str,
	) -> AccessPackageResourceScopesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_package_resource_scopes import AccessPackageResourceScopesRequest
		return AccessPackageResourceScopesRequest(self.request_adapter, path_parameters)

	def access_packages(self,
		accessPackageCatalog_id: str,
	) -> AccessPackagesRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .access_packages import AccessPackagesRequest
		return AccessPackagesRequest(self.request_adapter, path_parameters)

	def access_packages_with_uniquename(self,
		accessPackageCatalog_id: str,
		uniqueName: str,
	) -> AccessPackagesWithUniqueNameRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["uniqueName"] =  uniqueName

		from .access_packages_with_uniquename import AccessPackagesWithUniqueNameRequest
		return AccessPackagesWithUniqueNameRequest(self.request_adapter, path_parameters)

	def custom_access_package_workflow_extensions(self,
		accessPackageCatalog_id: str,
	) -> CustomAccessPackageWorkflowExtensionsRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .custom_access_package_workflow_extensions import CustomAccessPackageWorkflowExtensionsRequest
		return CustomAccessPackageWorkflowExtensionsRequest(self.request_adapter, path_parameters)

