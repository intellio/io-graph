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
	from .count import CountRequest
	from .by_user_p_f_x_certificate_id import ByUserPFXCertificateIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_p_f_x_certificate import UserPFXCertificate
from iograph_models.beta.user_p_f_x_certificate_collection_response import UserPFXCertificateCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UserPfxCertificatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userPfxCertificates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserPFXCertificateCollectionResponse:
		"""
		Get userPfxCertificates from deviceManagement
		Collection of PFX certificates associated with a user.
		"""
		tags = ['deviceManagement.userPFXCertificate']

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
		return await self.request_adapter.send_async(request_info, UserPFXCertificateCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserPFXCertificate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserPFXCertificate:
		"""
		Create new navigation property to userPfxCertificates for deviceManagement
		
		"""
		tags = ['deviceManagement.userPFXCertificate']

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
		return await self.request_adapter.send_async(request_info, UserPFXCertificate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserPfxCertificatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserPfxCertificatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserPfxCertificatesRequest(self.request_adapter, self.path_parameters)

	def by_user_p_f_x_certificate_id(self,
		userPFXCertificate_id: str,
	) -> ByUserPFXCertificateIdRequest:
		if userPFXCertificate_id is None:
			raise TypeError("userPFXCertificate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userPFXCertificate%2Did"] =  userPFXCertificate_id

		from .by_user_p_f_x_certificate_id import ByUserPFXCertificateIdRequest
		return ByUserPFXCertificateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

