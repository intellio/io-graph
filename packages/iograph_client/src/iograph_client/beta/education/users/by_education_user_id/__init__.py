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
	from .user import UserRequest
	from .taught_classes import TaughtClassesRequest
	from .schools import SchoolsRequest
	from .rubrics import RubricsRequest
	from .classes import ClassesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_user import EducationUser
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByEducationUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/users/{educationUser%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationUser:
		"""
		Get educationUser
		Retrieve the properties and relationships of a user.
		Find more info here: https://learn.microsoft.com/graph/api/educationuser-get?view=graph-rest-beta
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationUser, error_mapping)

	async def patch(
		self,
		body: EducationUser,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationUser:
		"""
		Update relatedContacts
		Update the relatedContact collection of an educationUser object.
		Find more info here: https://learn.microsoft.com/graph/api/relatedcontact-update?view=graph-rest-beta
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationUser, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete educationUser
		Delete a user.
		Find more info here: https://learn.microsoft.com/graph/api/educationuser-delete?view=graph-rest-beta
		"""
		tags = ['education.educationUser']
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



	def with_url(self, raw_url: str) -> ByEducationUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationUserIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		educationUser_id: str,
	) -> AssignmentsRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def classes(self,
		educationUser_id: str,
	) -> ClassesRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .classes import ClassesRequest
		return ClassesRequest(self.request_adapter, path_parameters)

	def rubrics(self,
		educationUser_id: str,
	) -> RubricsRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .rubrics import RubricsRequest
		return RubricsRequest(self.request_adapter, path_parameters)

	def schools(self,
		educationUser_id: str,
	) -> SchoolsRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .schools import SchoolsRequest
		return SchoolsRequest(self.request_adapter, path_parameters)

	def taught_classes(self,
		educationUser_id: str,
	) -> TaughtClassesRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .taught_classes import TaughtClassesRequest
		return TaughtClassesRequest(self.request_adapter, path_parameters)

	def user(self,
		educationUser_id: str,
	) -> UserRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id

		from .user import UserRequest
		return UserRequest(self.request_adapter, path_parameters)

