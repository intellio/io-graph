# Auto-generated client

from __future__ import annotations
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
	from .assignment import AssignmentRequest
	from .access_package import AccessPackageRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.access_package_assignment_request import AccessPackageAssignmentRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessPackageAssignmentRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentRequests/{accessPackageAssignmentRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentRequest:
		"""
		Get accessPackageAssignmentRequest
		In Microsoft Entra entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentrequest-get?view=graph-rest-1.0
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
		Delete accessPackageAssignmentRequest
		Delete an accessPackageAssignmentRequest object. This request can be made to remove a denied or completed request.  You cannot delete an access package assignment request if it has any accessPackageAssignment objects.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentrequest-delete?view=graph-rest-1.0
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

	@property
	def access_package(self,
	) -> AccessPackageRequest:
		from .access_package import AccessPackageRequest
		return AccessPackageRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment(self,
	) -> AssignmentRequest:
		from .assignment import AssignmentRequest
		return AssignmentRequest(self.request_adapter, self.path_parameters)

	@property
	def cancel(self,
	) -> CancelRequest:
		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, self.path_parameters)

	@property
	def reprocess(self,
	) -> ReprocessRequest:
		from .reprocess import ReprocessRequest
		return ReprocessRequest(self.request_adapter, self.path_parameters)

	@property
	def resume(self,
	) -> ResumeRequest:
		from .resume import ResumeRequest
		return ResumeRequest(self.request_adapter, self.path_parameters)

	@property
	def requestor(self,
	) -> RequestorRequest:
		from .requestor import RequestorRequest
		return RequestorRequest(self.request_adapter, self.path_parameters)

