# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_unified_role_definition_id1 import ByUnifiedRoleDefinitionId1Request
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.unified_role_definition import UnifiedRoleDefinition
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.unified_role_definition_collection_response import UnifiedRoleDefinitionCollectionResponse


class InheritsPermissionsFromRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/roleManagement/entitlementManagement/roleDefinitions/{unifiedRoleDefinition%2Did}/inheritsPermissionsFrom"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleDefinitionCollectionResponse:
		"""
		Get inheritsPermissionsFrom from roleManagement
		Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, UnifiedRoleDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: UnifiedRoleDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleDefinition:
		"""
		Create new navigation property to inheritsPermissionsFrom for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleDefinition, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_unified_role_definition_id1(self,
		unifiedRoleDefinition_id: str,
		unifiedRoleDefinition_id1: str,
	) -> ByUnifiedRoleDefinitionId1Request:
		if unifiedRoleDefinition_id is None:
			raise TypeError("unifiedRoleDefinition_id cannot be null.")
		if unifiedRoleDefinition_id1 is None:
			raise TypeError("unifiedRoleDefinition_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleDefinition%2Did"] =  unifiedRoleDefinition_id
		path_parameters["unifiedRoleDefinition%2Did1"] =  unifiedRoleDefinition_id1

		from .by_unified_role_definition_id1 import ByUnifiedRoleDefinitionId1Request
		return ByUnifiedRoleDefinitionId1Request(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

