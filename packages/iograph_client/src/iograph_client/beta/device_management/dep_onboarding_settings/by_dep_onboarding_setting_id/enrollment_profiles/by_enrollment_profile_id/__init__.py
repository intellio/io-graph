# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .update_device_profile_assignment import UpdateDeviceProfileAssignmentRequest
	from .set_default_profile import SetDefaultProfileRequest
	from .export_mobile_config import ExportMobileConfigRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.enrollment_profile import EnrollmentProfile
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByEnrollmentProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}/enrollmentProfiles/{enrollmentProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EnrollmentProfile:
		"""
		Get enrollmentProfiles from deviceManagement
		The enrollment profiles.
		"""
		tags = ['deviceManagement.depOnboardingSetting']

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
		return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)

	async def patch(
		self,
		body: EnrollmentProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EnrollmentProfile:
		"""
		Update the navigation property enrollmentProfiles in deviceManagement
		
		"""
		tags = ['deviceManagement.depOnboardingSetting']

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
		return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property enrollmentProfiles for deviceManagement
		
		"""
		tags = ['deviceManagement.depOnboardingSetting']
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



	def with_url(self, raw_url: str) -> ByEnrollmentProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEnrollmentProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEnrollmentProfileIdRequest(self.request_adapter, self.path_parameters)

	def export_mobile_config(self,
		depOnboardingSetting_id: str,
		enrollmentProfile_id: str,
	) -> ExportMobileConfigRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")
		if enrollmentProfile_id is None:
			raise TypeError("enrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id
		path_parameters["enrollmentProfile%2Did"] =  enrollmentProfile_id

		from .export_mobile_config import ExportMobileConfigRequest
		return ExportMobileConfigRequest(self.request_adapter, path_parameters)

	def set_default_profile(self,
		depOnboardingSetting_id: str,
		enrollmentProfile_id: str,
	) -> SetDefaultProfileRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")
		if enrollmentProfile_id is None:
			raise TypeError("enrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id
		path_parameters["enrollmentProfile%2Did"] =  enrollmentProfile_id

		from .set_default_profile import SetDefaultProfileRequest
		return SetDefaultProfileRequest(self.request_adapter, path_parameters)

	def update_device_profile_assignment(self,
		depOnboardingSetting_id: str,
		enrollmentProfile_id: str,
	) -> UpdateDeviceProfileAssignmentRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")
		if enrollmentProfile_id is None:
			raise TypeError("enrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id
		path_parameters["enrollmentProfile%2Did"] =  enrollmentProfile_id

		from .update_device_profile_assignment import UpdateDeviceProfileAssignmentRequest
		return UpdateDeviceProfileAssignmentRequest(self.request_adapter, path_parameters)

