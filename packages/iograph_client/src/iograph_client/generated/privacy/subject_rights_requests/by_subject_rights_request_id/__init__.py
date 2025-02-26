# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .team import TeamRequest
	from .notes import NotesRequest
	from .collaborators import CollaboratorsRequest
	from .approvers import ApproversRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.subject_rights_request import SubjectRightsRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySubjectRightsRequestIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/privacy/subjectRightsRequests/{subjectRightsRequest%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SubjectRightsRequest:
		"""
		Get subjectRightsRequest
		Read the properties and relationships of a subjectRightsRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/subjectrightsrequest-get?view=graph-rest-1.0
		"""
		tags = ['privacy.subjectRightsRequest']

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
		Update subjectRightsRequest
		Update the properties of a subjectRightsRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/subjectrightsrequest-update?view=graph-rest-1.0
		"""
		tags = ['privacy.subjectRightsRequest']

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
		Delete navigation property subjectRightsRequests for privacy
		
		"""
		tags = ['privacy.subjectRightsRequest']
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
	def approvers(self,
	) -> ApproversRequest:
		from .approvers import ApproversRequest
		return ApproversRequest(self.request_adapter, self.path_parameters)

	@property
	def collaborators(self,
	) -> CollaboratorsRequest:
		from .collaborators import CollaboratorsRequest
		return CollaboratorsRequest(self.request_adapter, self.path_parameters)

	@property
	def notes(self,
	) -> NotesRequest:
		from .notes import NotesRequest
		return NotesRequest(self.request_adapter, self.path_parameters)

	@property
	def team(self,
	) -> TeamRequest:
		from .team import TeamRequest
		return TeamRequest(self.request_adapter, self.path_parameters)

