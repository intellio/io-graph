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
	from .teachers import TeachersRequest
	from .schools import SchoolsRequest
	from .modules import ModulesRequest
	from .get_recently_modified_submissions import GetRecentlyModifiedSubmissionsRequest
	from .members import MembersRequest
	from .group import GroupRequest
	from .assignment_settings import AssignmentSettingsRequest
	from .assignments import AssignmentsRequest
	from .assignment_defaults import AssignmentDefaultsRequest
	from .assignment_categories import AssignmentCategoriesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.education_class import EducationClass


class ByEducationClassIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationClass:
		"""
		Get educationClass
		Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
		Find more info here: https://learn.microsoft.com/graph/api/educationclass-get?view=graph-rest-beta
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)

	async def patch(
		self,
		body: EducationClass,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationClass:
		"""
		Update educationclass properties
		Update the properties of a class.
		Find more info here: https://learn.microsoft.com/graph/api/educationclass-update?view=graph-rest-beta
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete educationClass
		Delete an educationClass. Because a class is also a universal group, deleting a class deletes the group.
		Find more info here: https://learn.microsoft.com/graph/api/educationclass-delete?view=graph-rest-beta
		"""
		tags = ['education.educationClass']
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



	def with_url(self, raw_url: str) -> ByEducationClassIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationClassIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationClassIdRequest(self.request_adapter, self.path_parameters)

	def assignment_categories(self,
		educationClass_id: str,
	) -> AssignmentCategoriesRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .assignment_categories import AssignmentCategoriesRequest
		return AssignmentCategoriesRequest(self.request_adapter, path_parameters)

	def assignment_defaults(self,
		educationClass_id: str,
	) -> AssignmentDefaultsRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .assignment_defaults import AssignmentDefaultsRequest
		return AssignmentDefaultsRequest(self.request_adapter, path_parameters)

	def assignments(self,
		educationClass_id: str,
	) -> AssignmentsRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def assignment_settings(self,
		educationClass_id: str,
	) -> AssignmentSettingsRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .assignment_settings import AssignmentSettingsRequest
		return AssignmentSettingsRequest(self.request_adapter, path_parameters)

	def group(self,
		educationClass_id: str,
	) -> GroupRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def members(self,
		educationClass_id: str,
	) -> MembersRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def get_recently_modified_submissions(self,
		educationClass_id: str,
	) -> GetRecentlyModifiedSubmissionsRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .get_recently_modified_submissions import GetRecentlyModifiedSubmissionsRequest
		return GetRecentlyModifiedSubmissionsRequest(self.request_adapter, path_parameters)

	def modules(self,
		educationClass_id: str,
	) -> ModulesRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .modules import ModulesRequest
		return ModulesRequest(self.request_adapter, path_parameters)

	def schools(self,
		educationClass_id: str,
	) -> SchoolsRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .schools import SchoolsRequest
		return SchoolsRequest(self.request_adapter, path_parameters)

	def teachers(self,
		educationClass_id: str,
	) -> TeachersRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .teachers import TeachersRequest
		return TeachersRequest(self.request_adapter, path_parameters)

