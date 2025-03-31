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
	from .remove_personal_data import RemovePersonalDataRequest
	from .export_personal_data import ExportPersonalDataRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.inbound_shared_user_profile import InboundSharedUserProfile
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByInboundSharedUserProfileUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/inboundSharedUserProfiles/{inboundSharedUserProfile%2DuserId}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InboundSharedUserProfile:
		"""
		Get inboundSharedUserProfile
		Read the properties of an inboundSharedUserProfile.
		Find more info here: https://learn.microsoft.com/graph/api/inboundshareduserprofile-get?view=graph-rest-beta
		"""
		tags = ['directory.inboundSharedUserProfile']

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
		return await self.request_adapter.send_async(request_info, InboundSharedUserProfile, error_mapping)

	async def patch(
		self,
		body: InboundSharedUserProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InboundSharedUserProfile:
		"""
		Update the navigation property inboundSharedUserProfiles in directory
		
		"""
		tags = ['directory.inboundSharedUserProfile']

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
		return await self.request_adapter.send_async(request_info, InboundSharedUserProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property inboundSharedUserProfiles for directory
		
		"""
		tags = ['directory.inboundSharedUserProfile']
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



	def with_url(self, raw_url: str) -> ByInboundSharedUserProfileUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByInboundSharedUserProfileUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByInboundSharedUserProfileUserIdRequest(self.request_adapter, self.path_parameters)

	def export_personal_data(self,
		inboundSharedUserProfile_userId: str,
	) -> ExportPersonalDataRequest:
		if inboundSharedUserProfile_userId is None:
			raise TypeError("inboundSharedUserProfile_userId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["inboundSharedUserProfile%2DuserId"] =  inboundSharedUserProfile_userId

		from .export_personal_data import ExportPersonalDataRequest
		return ExportPersonalDataRequest(self.request_adapter, path_parameters)

	def remove_personal_data(self,
		inboundSharedUserProfile_userId: str,
	) -> RemovePersonalDataRequest:
		if inboundSharedUserProfile_userId is None:
			raise TypeError("inboundSharedUserProfile_userId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["inboundSharedUserProfile%2DuserId"] =  inboundSharedUserProfile_userId

		from .remove_personal_data import RemovePersonalDataRequest
		return RemovePersonalDataRequest(self.request_adapter, path_parameters)

