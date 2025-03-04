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
	from .inherits_permissions_from import InheritsPermissionsFromRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.unified_role_definition import UnifiedRoleDefinition


class ByUnifiedRoleDefinitionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/directory/roleDefinitions/{unifiedRoleDefinition%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleDefinition:
		"""
		Get unifiedRoleDefinition
		Read the properties and relationships of a unifiedRoleDefinition object. The following role-based access control (RBAC) providers are currently supported:
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-get?view=graph-rest-1.0
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleDefinition, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleDefinition:
		"""
		Update unifiedRoleDefinition
		Update the properties of a unifiedRoleDefinition object. You cannot update built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-update?view=graph-rest-1.0
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleDefinition, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete unifiedRoleDefinition
		Delete a unifiedRoleDefinition object. You can't delete built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-delete?view=graph-rest-1.0
		"""
		tags = ['roleManagement.rbacApplication']
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



	def with_url(self, raw_url: str) -> ByUnifiedRoleDefinitionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRoleDefinitionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRoleDefinitionIdRequest(self.request_adapter, self.path_parameters)

	def inherits_permissions_from(self,
		unifiedRoleDefinition_id: str,
	) -> InheritsPermissionsFromRequest:
		if unifiedRoleDefinition_id is None:
			raise TypeError("unifiedRoleDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleDefinition%2Did"] =  unifiedRoleDefinition_id

		from .inherits_permissions_from import InheritsPermissionsFromRequest
		return InheritsPermissionsFromRequest(self.request_adapter, path_parameters)

