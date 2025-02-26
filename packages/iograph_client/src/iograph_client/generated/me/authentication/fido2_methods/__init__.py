# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_fido2_authentication_method_id import ByFido2AuthenticationMethodIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.fido2_authentication_method_collection_response import Fido2AuthenticationMethodCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class Fido2MethodsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/authentication/fido2Methods"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Fido2AuthenticationMethodCollectionResponse:
		"""
		List fido2AuthenticationMethod
		Retrieve a list of a user's FIDO2 Security Key Authentication Method objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/fido2authenticationmethod-list?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Fido2AuthenticationMethodCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def by_fido2_authentication_method_id(self,
		fido2AuthenticationMethod_id: str,
	) -> ByFido2AuthenticationMethodIdRequest:
		if fido2AuthenticationMethod_id is None:
			raise TypeError("fido2AuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fido2AuthenticationMethod%2Did"] =  fido2AuthenticationMethod_id

		from .by_fido2_authentication_method_id import ByFido2AuthenticationMethodIdRequest
		return ByFido2AuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

