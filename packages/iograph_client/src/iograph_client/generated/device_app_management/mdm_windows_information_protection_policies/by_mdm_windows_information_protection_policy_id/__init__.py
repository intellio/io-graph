# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy


class ByMdmWindowsInformationProtectionPolicyIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/mdmWindowsInformationProtectionPolicies/{mdmWindowsInformationProtectionPolicy%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MdmWindowsInformationProtectionPolicy:
		"""
		Get mdmWindowsInformationProtectionPolicy
		Read properties and relationships of the mdmWindowsInformationProtectionPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-mdmwindowsinformationprotectionpolicy-get?view=graph-rest-1.0
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
		Update mdmWindowsInformationProtectionPolicy
		Update the properties of a mdmWindowsInformationProtectionPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-mdmwindowsinformationprotectionpolicy-update?view=graph-rest-1.0
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
		Delete mdmWindowsInformationProtectionPolicy
		Deletes a mdmWindowsInformationProtectionPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-mdmwindowsinformationprotectionpolicy-delete?view=graph-rest-1.0
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



	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def exempt_app_locker_files(self,
	) -> ExemptAppLockerFilesRequest:
		from .exempt_app_locker_files import ExemptAppLockerFilesRequest
		return ExemptAppLockerFilesRequest(self.request_adapter, self.path_parameters)

	@property
	def protected_app_locker_files(self,
	) -> ProtectedAppLockerFilesRequest:
		from .protected_app_locker_files import ProtectedAppLockerFilesRequest
		return ProtectedAppLockerFilesRequest(self.request_adapter, self.path_parameters)

