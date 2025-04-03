# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .resources import ResourcesRequest
	from .unpin import UnpinRequest
	from .set_up_resources_folder import SetUpResourcesFolderRequest
	from .publish import PublishRequest
	from .pin import PinRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.education_module import EducationModule


class ByEducationModuleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/modules/{educationModule%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationModule:
		"""
		Get educationModule
		Get the properties and relationships of a module. Only teachers, students, and applications with application permissions can perform this operation. Students can only see published modules; teachers and applications with application permissions can see all modules in a class.
		Find more info here: https://learn.microsoft.com/graph/api/educationmodule-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)

	async def patch(
		self,
		body: EducationModule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationModule:
		"""
		Update educationModule
		Update an educationModule object in a class. Only teachers in the class can perform this operation. Note that you can't use a PATCH request to change the status of a module. Use the publish action to change the module status.
		Find more info here: https://learn.microsoft.com/graph/api/educationmodule-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete educationModule
		Delete an existing module in a class. Only teachers within a class can delete modules.
		Find more info here: https://learn.microsoft.com/graph/api/educationmodule-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByEducationModuleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationModuleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationModuleIdRequest(self.request_adapter, self.path_parameters)

	def pin(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> PinRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .pin import PinRequest
		return PinRequest(self.request_adapter, path_parameters)

	def publish(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> PublishRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, path_parameters)

	def set_up_resources_folder(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> SetUpResourcesFolderRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .set_up_resources_folder import SetUpResourcesFolderRequest
		return SetUpResourcesFolderRequest(self.request_adapter, path_parameters)

	def unpin(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> UnpinRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .unpin import UnpinRequest
		return UnpinRequest(self.request_adapter, path_parameters)

	def resources(self,
		educationClass_id: str,
		educationModule_id: str,
	) -> ResourcesRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationModule_id is None:
			raise TypeError("educationModule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationModule%2Did"] =  educationModule_id

		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, path_parameters)

