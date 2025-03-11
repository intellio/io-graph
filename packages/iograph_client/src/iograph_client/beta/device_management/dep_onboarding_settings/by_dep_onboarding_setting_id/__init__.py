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
	from .upload_dep_token import UploadDepTokenRequest
	from .unshare_for_school_data_sync_service import UnshareForSchoolDataSyncServiceRequest
	from .sync_with_apple_device_enrollment_program import SyncWithAppleDeviceEnrollmentProgramRequest
	from .share_for_school_data_sync_service import ShareForSchoolDataSyncServiceRequest
	from .get_encryption_public_key import GetEncryptionPublicKeyRequest
	from .generate_encryption_public_key import GenerateEncryptionPublicKeyRequest
	from .imported_apple_device_identities import ImportedAppleDeviceIdentitiesRequest
	from .enrollment_profiles import EnrollmentProfilesRequest
	from .default_vision_o_s_enrollment_profile import DefaultVisionOSEnrollmentProfileRequest
	from .default_tv_o_s_enrollment_profile import DefaultTvOSEnrollmentProfileRequest
	from .default_mac_os_enrollment_profile import DefaultMacOsEnrollmentProfileRequest
	from .default_ios_enrollment_profile import DefaultIosEnrollmentProfileRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.dep_onboarding_setting import DepOnboardingSetting


class ByDepOnboardingSettingIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DepOnboardingSetting:
		"""
		Get depOnboardingSettings from deviceManagement
		This collections of multiple DEP tokens per-tenant.
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
		return await self.request_adapter.send_async(request_info, DepOnboardingSetting, error_mapping)

	async def patch(
		self,
		body: DepOnboardingSetting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DepOnboardingSetting:
		"""
		Update the navigation property depOnboardingSettings in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, DepOnboardingSetting, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property depOnboardingSettings for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByDepOnboardingSettingIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDepOnboardingSettingIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDepOnboardingSettingIdRequest(self.request_adapter, self.path_parameters)

	def default_ios_enrollment_profile(self,
		depOnboardingSetting_id: str,
	) -> DefaultIosEnrollmentProfileRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .default_ios_enrollment_profile import DefaultIosEnrollmentProfileRequest
		return DefaultIosEnrollmentProfileRequest(self.request_adapter, path_parameters)

	def default_mac_os_enrollment_profile(self,
		depOnboardingSetting_id: str,
	) -> DefaultMacOsEnrollmentProfileRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .default_mac_os_enrollment_profile import DefaultMacOsEnrollmentProfileRequest
		return DefaultMacOsEnrollmentProfileRequest(self.request_adapter, path_parameters)

	def default_tv_o_s_enrollment_profile(self,
		depOnboardingSetting_id: str,
	) -> DefaultTvOSEnrollmentProfileRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .default_tv_o_s_enrollment_profile import DefaultTvOSEnrollmentProfileRequest
		return DefaultTvOSEnrollmentProfileRequest(self.request_adapter, path_parameters)

	def default_vision_o_s_enrollment_profile(self,
		depOnboardingSetting_id: str,
	) -> DefaultVisionOSEnrollmentProfileRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .default_vision_o_s_enrollment_profile import DefaultVisionOSEnrollmentProfileRequest
		return DefaultVisionOSEnrollmentProfileRequest(self.request_adapter, path_parameters)

	def enrollment_profiles(self,
		depOnboardingSetting_id: str,
	) -> EnrollmentProfilesRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .enrollment_profiles import EnrollmentProfilesRequest
		return EnrollmentProfilesRequest(self.request_adapter, path_parameters)

	def imported_apple_device_identities(self,
		depOnboardingSetting_id: str,
	) -> ImportedAppleDeviceIdentitiesRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .imported_apple_device_identities import ImportedAppleDeviceIdentitiesRequest
		return ImportedAppleDeviceIdentitiesRequest(self.request_adapter, path_parameters)

	def generate_encryption_public_key(self,
		depOnboardingSetting_id: str,
	) -> GenerateEncryptionPublicKeyRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .generate_encryption_public_key import GenerateEncryptionPublicKeyRequest
		return GenerateEncryptionPublicKeyRequest(self.request_adapter, path_parameters)

	def get_encryption_public_key(self,
		depOnboardingSetting_id: str,
	) -> GetEncryptionPublicKeyRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .get_encryption_public_key import GetEncryptionPublicKeyRequest
		return GetEncryptionPublicKeyRequest(self.request_adapter, path_parameters)

	def share_for_school_data_sync_service(self,
		depOnboardingSetting_id: str,
	) -> ShareForSchoolDataSyncServiceRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .share_for_school_data_sync_service import ShareForSchoolDataSyncServiceRequest
		return ShareForSchoolDataSyncServiceRequest(self.request_adapter, path_parameters)

	def sync_with_apple_device_enrollment_program(self,
		depOnboardingSetting_id: str,
	) -> SyncWithAppleDeviceEnrollmentProgramRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .sync_with_apple_device_enrollment_program import SyncWithAppleDeviceEnrollmentProgramRequest
		return SyncWithAppleDeviceEnrollmentProgramRequest(self.request_adapter, path_parameters)

	def unshare_for_school_data_sync_service(self,
		depOnboardingSetting_id: str,
	) -> UnshareForSchoolDataSyncServiceRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .unshare_for_school_data_sync_service import UnshareForSchoolDataSyncServiceRequest
		return UnshareForSchoolDataSyncServiceRequest(self.request_adapter, path_parameters)

	def upload_dep_token(self,
		depOnboardingSetting_id: str,
	) -> UploadDepTokenRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .upload_dep_token import UploadDepTokenRequest
		return UploadDepTokenRequest(self.request_adapter, path_parameters)

