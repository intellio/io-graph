# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sign_up import SignUpRequest
	from .is_signed_up import IsSignedUpRequest
	from .complete_setup import CompleteSetupRequest
	from .can_sign_up import CanSignUpRequest
	from .count import CountRequest
	from .by_privileged_signup_status_id import ByPrivilegedSignupStatusIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.privileged_signup_status import PrivilegedSignupStatus
from iograph_models.beta.privileged_signup_status_collection_response import PrivilegedSignupStatusCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PrivilegedSignupStatusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/privilegedSignupStatus", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedSignupStatusCollectionResponse:
		"""
		Get entities from privilegedSignupStatus
		
		"""
		tags = ['privilegedSignupStatus.privilegedSignupStatus']

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
		return await self.request_adapter.send_async(request_info, PrivilegedSignupStatusCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrivilegedSignupStatus,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedSignupStatus:
		"""
		Add new entity to privilegedSignupStatus
		
		"""
		tags = ['privilegedSignupStatus.privilegedSignupStatus']

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
		return await self.request_adapter.send_async(request_info, PrivilegedSignupStatus, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PrivilegedSignupStatusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PrivilegedSignupStatusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PrivilegedSignupStatusRequest(self.request_adapter, self.path_parameters)

	def by_privileged_signup_status_id(self,
		privilegedSignupStatus_id: str,
	) -> ByPrivilegedSignupStatusIdRequest:
		if privilegedSignupStatus_id is None:
			raise TypeError("privilegedSignupStatus_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedSignupStatus%2Did"] =  privilegedSignupStatus_id

		from .by_privileged_signup_status_id import ByPrivilegedSignupStatusIdRequest
		return ByPrivilegedSignupStatusIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def can_sign_up(self,
	) -> CanSignUpRequest:
		from .can_sign_up import CanSignUpRequest
		return CanSignUpRequest(self.request_adapter, self.path_parameters)

	@property
	def complete_setup(self,
	) -> CompleteSetupRequest:
		from .complete_setup import CompleteSetupRequest
		return CompleteSetupRequest(self.request_adapter, self.path_parameters)

	@property
	def is_signed_up(self,
	) -> IsSignedUpRequest:
		from .is_signed_up import IsSignedUpRequest
		return IsSignedUpRequest(self.request_adapter, self.path_parameters)

	@property
	def sign_up(self,
	) -> SignUpRequest:
		from .sign_up import SignUpRequest
		return SignUpRequest(self.request_adapter, self.path_parameters)

