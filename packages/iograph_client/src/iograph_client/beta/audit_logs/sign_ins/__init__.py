# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .confirm_safe import ConfirmSafeRequest
	from .confirm_compromised import ConfirmCompromisedRequest
	from .count import CountRequest
	from .by_sign_in_id import BySignInIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.sign_in import SignIn
from iograph_models.beta.sign_in_collection_response import SignInCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SignInsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/auditLogs/signIns", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SignInCollectionResponse:
		"""
		List signIns
		Get a list of signIn objects. The list contains the user sign-ins for your Microsoft Entra tenant. Sign-ins where a username and password are passed as part of authorization token, and successful federated sign-ins are currently included in the sign-in logs. The maximum and default page size is 1,000 objects and by default, the most recent sign-ins are returned first. Only sign-in events that occurred within the Microsoft Entra ID default retention period are available.
		Find more info here: https://learn.microsoft.com/graph/api/signin-list?view=graph-rest-beta
		"""
		tags = ['auditLogs.signIn']

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
		return await self.request_adapter.send_async(request_info, SignInCollectionResponse, error_mapping)

	async def post(
		self,
		body: SignIn,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SignIn:
		"""
		Create new navigation property to signIns for auditLogs
		
		"""
		tags = ['auditLogs.signIn']

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
		return await self.request_adapter.send_async(request_info, SignIn, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SignInsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SignInsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SignInsRequest(self.request_adapter, self.path_parameters)

	def by_sign_in_id(self,
		signIn_id: str,
	) -> BySignInIdRequest:
		if signIn_id is None:
			raise TypeError("signIn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["signIn%2Did"] =  signIn_id

		from .by_sign_in_id import BySignInIdRequest
		return BySignInIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def confirm_compromised(self,
	) -> ConfirmCompromisedRequest:
		from .confirm_compromised import ConfirmCompromisedRequest
		return ConfirmCompromisedRequest(self.request_adapter, self.path_parameters)

	@property
	def confirm_safe(self,
	) -> ConfirmSafeRequest:
		from .confirm_safe import ConfirmSafeRequest
		return ConfirmSafeRequest(self.request_adapter, self.path_parameters)

