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
	from .set_priority import SetPriorityRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByAppleUserInitiatedEnrollmentProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/appleUserInitiatedEnrollmentProfiles/{appleUserInitiatedEnrollmentProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppleUserInitiatedEnrollmentProfile:
		"""
		Get appleUserInitiatedEnrollmentProfiles from deviceManagement
		Apple user initiated enrollment profiles
		"""
		tags = ['deviceManagement.appleUserInitiatedEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AppleUserInitiatedEnrollmentProfile, error_mapping)

	async def patch(
		self,
		body: AppleUserInitiatedEnrollmentProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AppleUserInitiatedEnrollmentProfile:
		"""
		Update the navigation property appleUserInitiatedEnrollmentProfiles in deviceManagement
		
		"""
		tags = ['deviceManagement.appleUserInitiatedEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AppleUserInitiatedEnrollmentProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property appleUserInitiatedEnrollmentProfiles for deviceManagement
		
		"""
		tags = ['deviceManagement.appleUserInitiatedEnrollmentProfile']
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



	def with_url(self, raw_url: str) -> ByAppleUserInitiatedEnrollmentProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAppleUserInitiatedEnrollmentProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAppleUserInitiatedEnrollmentProfileIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		appleUserInitiatedEnrollmentProfile_id: str,
	) -> AssignmentsRequest:
		if appleUserInitiatedEnrollmentProfile_id is None:
			raise TypeError("appleUserInitiatedEnrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appleUserInitiatedEnrollmentProfile%2Did"] =  appleUserInitiatedEnrollmentProfile_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def set_priority(self,
		appleUserInitiatedEnrollmentProfile_id: str,
	) -> SetPriorityRequest:
		if appleUserInitiatedEnrollmentProfile_id is None:
			raise TypeError("appleUserInitiatedEnrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appleUserInitiatedEnrollmentProfile%2Did"] =  appleUserInitiatedEnrollmentProfile_id

		from .set_priority import SetPriorityRequest
		return SetPriorityRequest(self.request_adapter, path_parameters)

