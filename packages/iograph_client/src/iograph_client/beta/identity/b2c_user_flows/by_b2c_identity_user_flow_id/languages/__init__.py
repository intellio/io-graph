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
	from .count import CountRequest
	from .by_user_flow_language_configuration_id import ByUserFlowLanguageConfigurationIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user_flow_language_configuration_collection_response import UserFlowLanguageConfigurationCollectionResponse
from iograph_models.beta.user_flow_language_configuration import UserFlowLanguageConfiguration


class LanguagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}/languages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserFlowLanguageConfigurationCollectionResponse:
		"""
		List languages
		Retrieve a list of languages supported for customization in an Azure AD B2C user flow. Note: To retrieve a list of languages supported for customization, you must first enable language customization on your Azure AD B2C user flow. For more information, see Update b2cIdentityUserFlow.
		Find more info here: https://learn.microsoft.com/graph/api/b2cidentityuserflow-list-languages?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, UserFlowLanguageConfigurationCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserFlowLanguageConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserFlowLanguageConfiguration:
		"""
		Create new navigation property to languages for identity
		
		"""
		tags = ['identity.b2cIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, UserFlowLanguageConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LanguagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LanguagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LanguagesRequest(self.request_adapter, self.path_parameters)

	def by_user_flow_language_configuration_id(self,
		b2cIdentityUserFlow_id: str,
		userFlowLanguageConfiguration_id: str,
	) -> ByUserFlowLanguageConfigurationIdRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if userFlowLanguageConfiguration_id is None:
			raise TypeError("userFlowLanguageConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["userFlowLanguageConfiguration%2Did"] =  userFlowLanguageConfiguration_id

		from .by_user_flow_language_configuration_id import ByUserFlowLanguageConfigurationIdRequest
		return ByUserFlowLanguageConfigurationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		b2cIdentityUserFlow_id: str,
	) -> CountRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

