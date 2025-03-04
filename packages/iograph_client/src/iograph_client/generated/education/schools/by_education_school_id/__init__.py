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
	from .users import UsersRequest
	from .classes import ClassesRequest
	from .administrative_unit import AdministrativeUnitRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.education_school import EducationSchool


class ByEducationSchoolIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/schools/{educationSchool%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationSchool:
		"""
		Get educationSchool
		Read the properties and relationships of an educationSchool object.
		Find more info here: https://learn.microsoft.com/graph/api/educationschool-get?view=graph-rest-1.0
		"""
		tags = ['education.educationSchool']

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
		return await self.request_adapter.send_async(request_info, EducationSchool, error_mapping)

	async def patch(
		self,
		body: EducationSchool,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSchool:
		"""
		Update educationSchool
		Update the properties of an educationSchool object.
		Find more info here: https://learn.microsoft.com/graph/api/educationschool-update?view=graph-rest-1.0
		"""
		tags = ['education.educationSchool']

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
		return await self.request_adapter.send_async(request_info, EducationSchool, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete educationSchool
		Delete a school.
		Find more info here: https://learn.microsoft.com/graph/api/educationschool-delete?view=graph-rest-1.0
		"""
		tags = ['education.educationSchool']
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



	def with_url(self, raw_url: str) -> ByEducationSchoolIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationSchoolIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationSchoolIdRequest(self.request_adapter, self.path_parameters)

	def administrative_unit(self,
		educationSchool_id: str,
	) -> AdministrativeUnitRequest:
		if educationSchool_id is None:
			raise TypeError("educationSchool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationSchool%2Did"] =  educationSchool_id

		from .administrative_unit import AdministrativeUnitRequest
		return AdministrativeUnitRequest(self.request_adapter, path_parameters)

	def classes(self,
		educationSchool_id: str,
	) -> ClassesRequest:
		if educationSchool_id is None:
			raise TypeError("educationSchool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationSchool%2Did"] =  educationSchool_id

		from .classes import ClassesRequest
		return ClassesRequest(self.request_adapter, path_parameters)

	def users(self,
		educationSchool_id: str,
	) -> UsersRequest:
		if educationSchool_id is None:
			raise TypeError("educationSchool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationSchool%2Did"] =  educationSchool_id

		from .users import UsersRequest
		return UsersRequest(self.request_adapter, path_parameters)

