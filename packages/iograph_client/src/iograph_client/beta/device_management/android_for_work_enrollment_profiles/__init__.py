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
	from .by_android_for_work_enrollment_profile_id import ByAndroidForWorkEnrollmentProfileIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.android_for_work_enrollment_profile_collection_response import AndroidForWorkEnrollmentProfileCollectionResponse
from iograph_models.beta.android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile


class AndroidForWorkEnrollmentProfilesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/androidForWorkEnrollmentProfiles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AndroidForWorkEnrollmentProfileCollectionResponse:
		"""
		Get androidForWorkEnrollmentProfiles from deviceManagement
		Android for Work enrollment profile entities.
		"""
		tags = ['deviceManagement.androidForWorkEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AndroidForWorkEnrollmentProfileCollectionResponse, error_mapping)

	async def post(
		self,
		body: AndroidForWorkEnrollmentProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AndroidForWorkEnrollmentProfile:
		"""
		Create new navigation property to androidForWorkEnrollmentProfiles for deviceManagement
		
		"""
		tags = ['deviceManagement.androidForWorkEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AndroidForWorkEnrollmentProfile, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AndroidForWorkEnrollmentProfilesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AndroidForWorkEnrollmentProfilesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AndroidForWorkEnrollmentProfilesRequest(self.request_adapter, self.path_parameters)

	def by_android_for_work_enrollment_profile_id(self,
		androidForWorkEnrollmentProfile_id: str,
	) -> ByAndroidForWorkEnrollmentProfileIdRequest:
		if androidForWorkEnrollmentProfile_id is None:
			raise TypeError("androidForWorkEnrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidForWorkEnrollmentProfile%2Did"] =  androidForWorkEnrollmentProfile_id

		from .by_android_for_work_enrollment_profile_id import ByAndroidForWorkEnrollmentProfileIdRequest
		return ByAndroidForWorkEnrollmentProfileIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

