# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_user_flow_language_page_id import ByUserFlowLanguagePageIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_flow_language_page_collection_response import UserFlowLanguagePageCollectionResponse
from iograph_models.beta.user_flow_language_page import UserFlowLanguagePage
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DefaultPagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}/languages/{userFlowLanguageConfiguration%2Did}/defaultPages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserFlowLanguagePageCollectionResponse:
		"""
		List defaultPages
		Get the userFlowLanguagePage resources from the defaultPages navigation property. These contain the values shown to the user in a default user journey of a user flow.
		Find more info here: https://learn.microsoft.com/graph/api/userflowlanguageconfiguration-list-defaultpages?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, UserFlowLanguagePageCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserFlowLanguagePage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserFlowLanguagePage:
		"""
		Create new navigation property to defaultPages for identity
		
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
		return await self.request_adapter.send_async(request_info, UserFlowLanguagePage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DefaultPagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DefaultPagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DefaultPagesRequest(self.request_adapter, self.path_parameters)

	def by_user_flow_language_page_id(self,
		b2cIdentityUserFlow_id: str,
		userFlowLanguageConfiguration_id: str,
		userFlowLanguagePage_id: str,
	) -> ByUserFlowLanguagePageIdRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if userFlowLanguageConfiguration_id is None:
			raise TypeError("userFlowLanguageConfiguration_id cannot be null.")
		if userFlowLanguagePage_id is None:
			raise TypeError("userFlowLanguagePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["userFlowLanguageConfiguration%2Did"] =  userFlowLanguageConfiguration_id
		path_parameters["userFlowLanguagePage%2Did"] =  userFlowLanguagePage_id

		from .by_user_flow_language_page_id import ByUserFlowLanguagePageIdRequest
		return ByUserFlowLanguagePageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		b2cIdentityUserFlow_id: str,
		userFlowLanguageConfiguration_id: str,
	) -> CountRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if userFlowLanguageConfiguration_id is None:
			raise TypeError("userFlowLanguageConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["userFlowLanguageConfiguration%2Did"] =  userFlowLanguageConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

