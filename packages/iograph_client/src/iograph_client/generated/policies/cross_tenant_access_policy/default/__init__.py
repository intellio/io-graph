# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .reset_to_system_default import ResetToSystemDefaultRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class DefaultRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/policies/crossTenantAccessPolicy/default"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CrossTenantAccessPolicyConfigurationDefault:
		"""
		Get crossTenantAccessPolicyConfigurationDefault
		Read the default configuration of a cross-tenant access policy. This default configuration may be the service default assigned by Microsoft Entra ID (isServiceDefault is true) or may be customized in your tenant (isServiceDefault is false).
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicyconfigurationdefault-get?view=graph-rest-1.0
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationDefault, error_mapping)

	async def patch(
		self,
		body: CrossTenantAccessPolicyConfigurationDefault,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CrossTenantAccessPolicyConfigurationDefault:
		"""
		Update crossTenantAccessPolicyConfigurationDefault
		Update the default configuration of a cross-tenant access policy.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicyconfigurationdefault-update?view=graph-rest-1.0
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationDefault, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property default for policies
		
		"""
		tags = ['policies.crossTenantAccessPolicy']
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
	def reset_to_system_default(self,
	) -> ResetToSystemDefaultRequest:
		from .reset_to_system_default import ResetToSystemDefaultRequest
		return ResetToSystemDefaultRequest(self.request_adapter, self.path_parameters)

