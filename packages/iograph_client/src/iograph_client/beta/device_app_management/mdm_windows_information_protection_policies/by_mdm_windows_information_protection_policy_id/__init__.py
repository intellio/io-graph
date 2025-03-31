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
	from .protected_app_locker_files import ProtectedAppLockerFilesRequest
	from .exempt_app_locker_files import ExemptAppLockerFilesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMdmWindowsInformationProtectionPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mdmWindowsInformationProtectionPolicies/{mdmWindowsInformationProtectionPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MdmWindowsInformationProtectionPolicy:
		"""
		Get mdmWindowsInformationProtectionPolicies from deviceAppManagement
		Windows information protection for apps running on devices which are MDM enrolled.
		"""
		tags = ['deviceAppManagement.mdmWindowsInformationProtectionPolicy']

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
		return await self.request_adapter.send_async(request_info, MdmWindowsInformationProtectionPolicy, error_mapping)

	async def patch(
		self,
		body: MdmWindowsInformationProtectionPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MdmWindowsInformationProtectionPolicy:
		"""
		Update the navigation property mdmWindowsInformationProtectionPolicies in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mdmWindowsInformationProtectionPolicy']

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
		return await self.request_adapter.send_async(request_info, MdmWindowsInformationProtectionPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property mdmWindowsInformationProtectionPolicies for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mdmWindowsInformationProtectionPolicy']
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



	def with_url(self, raw_url: str) -> ByMdmWindowsInformationProtectionPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMdmWindowsInformationProtectionPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMdmWindowsInformationProtectionPolicyIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		mdmWindowsInformationProtectionPolicy_id: str,
	) -> AssignmentsRequest:
		if mdmWindowsInformationProtectionPolicy_id is None:
			raise TypeError("mdmWindowsInformationProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mdmWindowsInformationProtectionPolicy%2Did"] =  mdmWindowsInformationProtectionPolicy_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def exempt_app_locker_files(self,
		mdmWindowsInformationProtectionPolicy_id: str,
	) -> ExemptAppLockerFilesRequest:
		if mdmWindowsInformationProtectionPolicy_id is None:
			raise TypeError("mdmWindowsInformationProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mdmWindowsInformationProtectionPolicy%2Did"] =  mdmWindowsInformationProtectionPolicy_id

		from .exempt_app_locker_files import ExemptAppLockerFilesRequest
		return ExemptAppLockerFilesRequest(self.request_adapter, path_parameters)

	def protected_app_locker_files(self,
		mdmWindowsInformationProtectionPolicy_id: str,
	) -> ProtectedAppLockerFilesRequest:
		if mdmWindowsInformationProtectionPolicy_id is None:
			raise TypeError("mdmWindowsInformationProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mdmWindowsInformationProtectionPolicy%2Did"] =  mdmWindowsInformationProtectionPolicy_id

		from .protected_app_locker_files import ProtectedAppLockerFilesRequest
		return ProtectedAppLockerFilesRequest(self.request_adapter, path_parameters)

