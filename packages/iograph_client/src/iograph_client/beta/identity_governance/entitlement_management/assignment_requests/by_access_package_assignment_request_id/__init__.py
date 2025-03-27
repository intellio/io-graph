# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .requestor import RequestorRequest
	from .resume import ResumeRequest
	from .reprocess import ReprocessRequest
	from .cancel import CancelRequest
	from .access_package_assignment import AccessPackageAssignmentRequest
	from .access_package import AccessPackageRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_assignment_request import AccessPackageAssignmentRequest


class ByAccessPackageAssignmentRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentRequests/{accessPackageAssignmentRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentRequest:
		"""
		Get assignmentRequests from identityGovernance
		Represents access package assignment requests created by or on behalf of a user.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentRequest, error_mapping)

	async def patch(
		self,
		body: AccessPackageAssignmentRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageAssignmentRequest:
		"""
		Update the navigation property assignmentRequests in identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignmentRequests for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']
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



	def with_url(self, raw_url: str) -> ByAccessPackageAssignmentRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageAssignmentRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageAssignmentRequestIdRequest(self.request_adapter, self.path_parameters)

	def access_package(self,
		accessPackageAssignmentRequest_id: str,
	) -> AccessPackageRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .access_package import AccessPackageRequest
		return AccessPackageRequest(self.request_adapter, path_parameters)

	def access_package_assignment(self,
		accessPackageAssignmentRequest_id: str,
	) -> AccessPackageAssignmentRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .access_package_assignment import AccessPackageAssignmentRequest
		return AccessPackageAssignmentRequest(self.request_adapter, path_parameters)

	def cancel(self,
		accessPackageAssignmentRequest_id: str,
	) -> CancelRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def reprocess(self,
		accessPackageAssignmentRequest_id: str,
	) -> ReprocessRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .reprocess import ReprocessRequest
		return ReprocessRequest(self.request_adapter, path_parameters)

	def resume(self,
		accessPackageAssignmentRequest_id: str,
	) -> ResumeRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .resume import ResumeRequest
		return ResumeRequest(self.request_adapter, path_parameters)

	def requestor(self,
		accessPackageAssignmentRequest_id: str,
	) -> RequestorRequest:
		if accessPackageAssignmentRequest_id is None:
			raise TypeError("accessPackageAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentRequest%2Did"] =  accessPackageAssignmentRequest_id

		from .requestor import RequestorRequest
		return RequestorRequest(self.request_adapter, path_parameters)

