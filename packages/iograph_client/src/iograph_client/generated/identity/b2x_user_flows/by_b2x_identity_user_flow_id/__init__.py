# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_flow_identity_providers import UserFlowIdentityProvidersRequest
	from .user_attribute_assignments import UserAttributeAssignmentsRequest
	from .languages import LanguagesRequest
	from .identity_providers import IdentityProvidersRequest
	from .api_connector_configuration import ApiConnectorConfigurationRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.b2x_identity_user_flow import B2xIdentityUserFlow


class ByB2xIdentityUserFlowIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> B2xIdentityUserFlow:
		"""
		Get b2xIdentityUserFlow
		Retrieve the properties and relationships of a b2xIdentityUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-get?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, B2xIdentityUserFlow, error_mapping)

	async def patch(
		self,
		body: B2xIdentityUserFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> B2xIdentityUserFlow:
		"""
		Update the navigation property b2xUserFlows in identity
		
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, B2xIdentityUserFlow, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete b2xIdentityUserFlow
		Delete a b2xIdentityUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-delete?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']
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
	def api_connector_configuration(self,
	) -> ApiConnectorConfigurationRequest:
		from .api_connector_configuration import ApiConnectorConfigurationRequest
		return ApiConnectorConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_providers(self,
	) -> IdentityProvidersRequest:
		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

	@property
	def languages(self,
	) -> LanguagesRequest:
		from .languages import LanguagesRequest
		return LanguagesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_attribute_assignments(self,
	) -> UserAttributeAssignmentsRequest:
		from .user_attribute_assignments import UserAttributeAssignmentsRequest
		return UserAttributeAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_flow_identity_providers(self,
	) -> UserFlowIdentityProvidersRequest:
		from .user_flow_identity_providers import UserFlowIdentityProvidersRequest
		return UserFlowIdentityProvidersRequest(self.request_adapter, self.path_parameters)

