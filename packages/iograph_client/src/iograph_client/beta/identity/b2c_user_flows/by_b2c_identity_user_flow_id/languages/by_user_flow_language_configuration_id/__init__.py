# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .overrides_pages import OverridesPagesRequest
	from .default_pages import DefaultPagesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_flow_language_configuration import UserFlowLanguageConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserFlowLanguageConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}/languages/{userFlowLanguageConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserFlowLanguageConfiguration:
		"""
		Get userFlowLanguageConfiguration
		Read the properties and relationships of a userFlowLanguageConfiguration object. These objects represent a language available in a user flow. Note: To retrieve a language supported for customization, you must first enable language customization on your Azure AD B2C user flow. For more information, see Update b2cIdentityUserFlow. Language customization is enabled by default in Microsoft Entra user flows.
		Find more info here: https://learn.microsoft.com/graph/api/userflowlanguageconfiguration-get?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, UserFlowLanguageConfiguration, error_mapping)

	async def patch(
		self,
		body: UserFlowLanguageConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserFlowLanguageConfiguration:
		"""
		Create or update language
		This method is used to create or update a custom language in an Azure AD B2C user flow. Note: You must enable language customization in the Azure AD B2C user flow before you can create a custom language. For more information, see Update b2cIdentityUserFlow.
		Find more info here: https://learn.microsoft.com/graph/api/b2cidentityuserflow-put-languages?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, UserFlowLanguageConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete userFlowLanguageConfiguration
		Deletes a userFlowLanguageConfiguration object from a Azure AD B2C user flow. Note: You cannot delete languages from an Microsoft Entra user flow.
		Find more info here: https://learn.microsoft.com/graph/api/userflowlanguageconfiguration-delete?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']
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



	def with_url(self, raw_url: str) -> ByUserFlowLanguageConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserFlowLanguageConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserFlowLanguageConfigurationIdRequest(self.request_adapter, self.path_parameters)

	def default_pages(self,
		b2cIdentityUserFlow_id: str,
		userFlowLanguageConfiguration_id: str,
	) -> DefaultPagesRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if userFlowLanguageConfiguration_id is None:
			raise TypeError("userFlowLanguageConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["userFlowLanguageConfiguration%2Did"] =  userFlowLanguageConfiguration_id

		from .default_pages import DefaultPagesRequest
		return DefaultPagesRequest(self.request_adapter, path_parameters)

	def overrides_pages(self,
		b2cIdentityUserFlow_id: str,
		userFlowLanguageConfiguration_id: str,
	) -> OverridesPagesRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if userFlowLanguageConfiguration_id is None:
			raise TypeError("userFlowLanguageConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["userFlowLanguageConfiguration%2Did"] =  userFlowLanguageConfiguration_id

		from .overrides_pages import OverridesPagesRequest
		return OverridesPagesRequest(self.request_adapter, path_parameters)

