# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
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
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_user import EducationUser
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/me", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationUser:
		"""
		Get me from education
		
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
		Update the navigation property me in education
		
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
		Delete navigation property me for education
		
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



	def with_url(self, raw_url: str) -> MeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MeRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def classes(self,
	) -> ClassesRequest:
		from .classes import ClassesRequest
		return ClassesRequest(self.request_adapter, self.path_parameters)

	@property
	def rubrics(self,
	) -> RubricsRequest:
		from .rubrics import RubricsRequest
		return RubricsRequest(self.request_adapter, self.path_parameters)

	@property
	def schools(self,
	) -> SchoolsRequest:
		from .schools import SchoolsRequest
		return SchoolsRequest(self.request_adapter, self.path_parameters)

	@property
	def taught_classes(self,
	) -> TaughtClassesRequest:
		from .taught_classes import TaughtClassesRequest
		return TaughtClassesRequest(self.request_adapter, self.path_parameters)

	@property
	def user(self,
	) -> UserRequest:
		from .user import UserRequest
		return UserRequest(self.request_adapter, self.path_parameters)

