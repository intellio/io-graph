# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_phone_authentication_method_id import ByPhoneAuthenticationMethodIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.phone_authentication_method import PhoneAuthenticationMethod
from iograph_models.models.phone_authentication_method_collection_response import PhoneAuthenticationMethodCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class PhoneMethodsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/authentication/phoneMethods"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PhoneAuthenticationMethodCollectionResponse:
		"""
		Get phoneMethods from users
		The phone numbers registered to a user for authentication.
		"""
		tags = ['users.authentication']

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
		return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethodCollectionResponse, error_mapping)

	async def post(
		self,
		body: PhoneAuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PhoneAuthenticationMethod:
		"""
		Create phoneMethod
		Add a new phone authentication method for a user. A user may only have one phone of each type, captured in the phoneType property. This means, for example, adding a mobile phone to a user with a pre-existing mobile phone fails. Additionally, a user must always have a mobile phone before adding an alternateMobile phone. Adding a phone number makes it available for use in both Azure multi-factor authentication (MFA) and self-service password reset (SSPR), if enabled. Additionally, if a user is enabled by policy to use SMS sign-in and a mobile number is added, the system attempts to register the number for use in that system.
		Find more info here: https://learn.microsoft.com/graph/api/authentication-post-phonemethods?view=graph-rest-1.0
		"""
		tags = ['users.authentication']

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
		return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethod, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_phone_authentication_method_id(self,
		user_id: str,
		phoneAuthenticationMethod_id: str,
	) -> ByPhoneAuthenticationMethodIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if phoneAuthenticationMethod_id is None:
			raise TypeError("phoneAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["phoneAuthenticationMethod%2Did"] =  phoneAuthenticationMethod_id

		from .by_phone_authentication_method_id import ByPhoneAuthenticationMethodIdRequest
		return ByPhoneAuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

