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
	from .count import CountRequest
	from .by_education_module_id import ByEducationModuleIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.education_module import EducationModule
from iograph_models.models.education_module_collection_response import EducationModuleCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ModulesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/modules", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationModuleCollectionResponse:
		"""
		List class modules
		Retrieve a list of module objects. Only teachers, students, and applications with application permissions can perform this operation. A teacher or an application with application permissions can see all module objects for the class. Students can only see published modules.
		Find more info here: https://learn.microsoft.com/graph/api/educationclass-list-modules?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, EducationModuleCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationModule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationModule:
		"""
		Create educationModule
		Create a new module in a class. Only teachers in a class can create a module. Modules start in the draft state, which means that students can't see the modules until publication.
		Find more info here: https://learn.microsoft.com/graph/api/educationclass-post-module?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ModulesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ModulesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ModulesRequest(self.request_adapter, self.path_parameters)

	def by_education_module_id(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> ByEducationModuleIdRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .by_education_module_id import ByEducationModuleIdRequest
		return ByEducationModuleIdRequest(self.request_adapter, path_parameters)

	def count(self,
		educationClass_id: str,
	) -> CountRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

