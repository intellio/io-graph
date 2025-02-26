# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .users import UsersRequest
	from .schools import SchoolsRequest
	from .me import MeRequest
	from .classes import ClassesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.education_root import EducationRoot
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class EducationRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/education"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationRoot:
		"""
		Get education
		
		"""
		tags = ['education.educationRoot']

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
		return await self.request_adapter.send_async(request_info, EducationRoot, error_mapping)

	async def patch(
		self,
		body: EducationRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationRoot:
		"""
		Update education
		
		"""
		tags = ['education.educationRoot']

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
		return await self.request_adapter.send_async(request_info, EducationRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def classes(self,
	) -> ClassesRequest:
		from .classes import ClassesRequest
		return ClassesRequest(self.request_adapter, self.path_parameters)

	@property
	def me(self,
	) -> MeRequest:
		from .me import MeRequest
		return MeRequest(self.request_adapter, self.path_parameters)

	@property
	def schools(self,
	) -> SchoolsRequest:
		from .schools import SchoolsRequest
		return SchoolsRequest(self.request_adapter, self.path_parameters)

	@property
	def users(self,
	) -> UsersRequest:
		from .users import UsersRequest
		return UsersRequest(self.request_adapter, self.path_parameters)

