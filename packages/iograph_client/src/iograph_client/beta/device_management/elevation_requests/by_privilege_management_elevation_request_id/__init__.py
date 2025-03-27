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
	from .revoke import RevokeRequest
	from .get_all_elevation_requests import GetAllElevationRequestsRequest
	from .deny import DenyRequest
	from .approve import ApproveRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.privilege_management_elevation_request import PrivilegeManagementElevationRequest


class ByPrivilegeManagementElevationRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/elevationRequests/{privilegeManagementElevationRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegeManagementElevationRequest:
		"""
		Get elevationRequests from deviceManagement
		List of elevation requests
		"""
		tags = ['deviceManagement.privilegeManagementElevationRequest']

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
		return await self.request_adapter.send_async(request_info, PrivilegeManagementElevationRequest, error_mapping)

	async def patch(
		self,
		body: PrivilegeManagementElevationRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegeManagementElevationRequest:
		"""
		Update the navigation property elevationRequests in deviceManagement
		
		"""
		tags = ['deviceManagement.privilegeManagementElevationRequest']

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
		return await self.request_adapter.send_async(request_info, PrivilegeManagementElevationRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property elevationRequests for deviceManagement
		
		"""
		tags = ['deviceManagement.privilegeManagementElevationRequest']
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



	def with_url(self, raw_url: str) -> ByPrivilegeManagementElevationRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegeManagementElevationRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegeManagementElevationRequestIdRequest(self.request_adapter, self.path_parameters)

	def approve(self,
		privilegeManagementElevationRequest_id: str,
	) -> ApproveRequest:
		if privilegeManagementElevationRequest_id is None:
			raise TypeError("privilegeManagementElevationRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegeManagementElevationRequest%2Did"] =  privilegeManagementElevationRequest_id

		from .approve import ApproveRequest
		return ApproveRequest(self.request_adapter, path_parameters)

	def deny(self,
		privilegeManagementElevationRequest_id: str,
	) -> DenyRequest:
		if privilegeManagementElevationRequest_id is None:
			raise TypeError("privilegeManagementElevationRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegeManagementElevationRequest%2Did"] =  privilegeManagementElevationRequest_id

		from .deny import DenyRequest
		return DenyRequest(self.request_adapter, path_parameters)

	def get_all_elevation_requests(self,
		privilegeManagementElevationRequest_id: str,
	) -> GetAllElevationRequestsRequest:
		if privilegeManagementElevationRequest_id is None:
			raise TypeError("privilegeManagementElevationRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegeManagementElevationRequest%2Did"] =  privilegeManagementElevationRequest_id

		from .get_all_elevation_requests import GetAllElevationRequestsRequest
		return GetAllElevationRequestsRequest(self.request_adapter, path_parameters)

	def revoke(self,
		privilegeManagementElevationRequest_id: str,
	) -> RevokeRequest:
		if privilegeManagementElevationRequest_id is None:
			raise TypeError("privilegeManagementElevationRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegeManagementElevationRequest%2Did"] =  privilegeManagementElevationRequest_id

		from .revoke import RevokeRequest
		return RevokeRequest(self.request_adapter, path_parameters)

