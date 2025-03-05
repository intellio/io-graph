# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_education_module_resource_id import ByEducationModuleResourceIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.education_module_resource import EducationModuleResource
from iograph_models.models.education_module_resource_collection_response import EducationModuleResourceCollectionResponse


class ResourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/modules/{educationModule%2Did}/resources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationModuleResourceCollectionResponse:
		"""
		List module resources
		Get all the educationModuleResource objects associated with a module. Only teachers, students, and applications with application permissions can perform this operation.
		Find more info here: https://learn.microsoft.com/graph/api/educationmodule-list-resources?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, EducationModuleResourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationModuleResource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationModuleResource:
		"""
		Create educationModuleResource
		Create a resource in a module. Only teachers can perform this operation. You can create the following types of module resources: Every resource has an @odata.type property to indicate which type of resource is being created.
		Find more info here: https://learn.microsoft.com/graph/api/educationmodule-post-resources?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, EducationModuleResource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ResourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	def by_education_module_resource_id(self,
		educationClass_id: str,
		educationModule_id: str,
		educationModuleResource_id: str,
	) -> ByEducationModuleResourceIdRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")
		if educationModuleResource_id is None:
			raise TypeError("educationModuleResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id
		path_parameters["educationModuleResource%2Did"] =  educationModuleResource_id

		from .by_education_module_resource_id import ByEducationModuleResourceIdRequest
		return ByEducationModuleResourceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> CountRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

