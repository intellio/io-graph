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
	from .team import TeamRequest
	from .notes import NotesRequest
	from .get_final_report import GetFinalReportRequest
	from .get_final_attachment import GetFinalAttachmentRequest
	from .collaborators_with_userprincipalname import CollaboratorsWithUserPrincipalNameRequest
	from .collaborators import CollaboratorsRequest
	from .approvers_with_userprincipalname import ApproversWithUserPrincipalNameRequest
	from .approvers import ApproversRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.subject_rights_request import SubjectRightsRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySubjectRightsRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/subjectRightsRequests/{subjectRightsRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SubjectRightsRequest:
		"""
		Get subjectRightsRequests from security
		
		"""
		tags = ['security.subjectRightsRequest']

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
		return await self.request_adapter.send_async(request_info, SubjectRightsRequest, error_mapping)

	async def patch(
		self,
		body: SubjectRightsRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SubjectRightsRequest:
		"""
		Update the navigation property subjectRightsRequests in security
		
		"""
		tags = ['security.subjectRightsRequest']

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
		return await self.request_adapter.send_async(request_info, SubjectRightsRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property subjectRightsRequests for security
		
		"""
		tags = ['security.subjectRightsRequest']
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



	def with_url(self, raw_url: str) -> BySubjectRightsRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySubjectRightsRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySubjectRightsRequestIdRequest(self.request_adapter, self.path_parameters)

	def approvers(self,
		subjectRightsRequest_id: str,
	) -> ApproversRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .approvers import ApproversRequest
		return ApproversRequest(self.request_adapter, path_parameters)

	def approvers_with_userprincipalname(self,
		subjectRightsRequest_id: str,
		userPrincipalName: str,
	) -> ApproversWithUserPrincipalNameRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")
		if userPrincipalName is None:
			raise TypeError("userPrincipalName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id
		path_parameters["userPrincipalName"] =  userPrincipalName

		from .approvers_with_userprincipalname import ApproversWithUserPrincipalNameRequest
		return ApproversWithUserPrincipalNameRequest(self.request_adapter, path_parameters)

	def collaborators(self,
		subjectRightsRequest_id: str,
	) -> CollaboratorsRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .collaborators import CollaboratorsRequest
		return CollaboratorsRequest(self.request_adapter, path_parameters)

	def collaborators_with_userprincipalname(self,
		subjectRightsRequest_id: str,
		userPrincipalName: str,
	) -> CollaboratorsWithUserPrincipalNameRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")
		if userPrincipalName is None:
			raise TypeError("userPrincipalName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id
		path_parameters["userPrincipalName"] =  userPrincipalName

		from .collaborators_with_userprincipalname import CollaboratorsWithUserPrincipalNameRequest
		return CollaboratorsWithUserPrincipalNameRequest(self.request_adapter, path_parameters)

	def get_final_attachment(self,
		subjectRightsRequest_id: str,
	) -> GetFinalAttachmentRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .get_final_attachment import GetFinalAttachmentRequest
		return GetFinalAttachmentRequest(self.request_adapter, path_parameters)

	def get_final_report(self,
		subjectRightsRequest_id: str,
	) -> GetFinalReportRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .get_final_report import GetFinalReportRequest
		return GetFinalReportRequest(self.request_adapter, path_parameters)

	def notes(self,
		subjectRightsRequest_id: str,
	) -> NotesRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .notes import NotesRequest
		return NotesRequest(self.request_adapter, path_parameters)

	def team(self,
		subjectRightsRequest_id: str,
	) -> TeamRequest:
		if subjectRightsRequest_id is None:
			raise TypeError("subjectRightsRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subjectRightsRequest%2Did"] =  subjectRightsRequest_id

		from .team import TeamRequest
		return TeamRequest(self.request_adapter, path_parameters)

