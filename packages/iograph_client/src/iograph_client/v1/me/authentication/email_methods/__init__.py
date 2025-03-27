# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_email_authentication_method_id import ByEmailAuthenticationMethodIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.email_authentication_method_collection_response import EmailAuthenticationMethodCollectionResponse
from iograph_models.v1.email_authentication_method import EmailAuthenticationMethod
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class EmailMethodsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/authentication/emailMethods", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EmailAuthenticationMethodCollectionResponse:
		"""
		List emailMethods
		Retrieve a list of a user's email Authentication Method objects and their properties. This call only returns a single object referenced by ID 3ddfcfc8-9383-446f-83cc-3ab9be4be18f as only one email method can be set on users.
		Find more info here: https://learn.microsoft.com/graph/api/authentication-list-emailmethods?view=graph-rest-1.0
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, EmailAuthenticationMethodCollectionResponse, error_mapping)

	async def post(
		self,
		body: EmailAuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EmailAuthenticationMethod:
		"""
		Create new navigation property to emailMethods for me
		
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, EmailAuthenticationMethod, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> EmailMethodsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EmailMethodsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EmailMethodsRequest(self.request_adapter, self.path_parameters)

	def by_email_authentication_method_id(self,
		emailAuthenticationMethod_id: str,
	) -> ByEmailAuthenticationMethodIdRequest:
		if emailAuthenticationMethod_id is None:
			raise TypeError("emailAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["emailAuthenticationMethod%2Did"] =  emailAuthenticationMethod_id

		from .by_email_authentication_method_id import ByEmailAuthenticationMethodIdRequest
		return ByEmailAuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

