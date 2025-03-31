# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .controls import ControlsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.program import Program
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByProgramIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/programs/{program%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Program:
		"""
		Get entity from programs by key
		
		"""
		tags = ['programs.program']

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
		return await self.request_adapter.send_async(request_info, Program, error_mapping)

	async def patch(
		self,
		body: Program,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Program:
		"""
		Update program (deprecated)
		In the Microsoft Entra access reviews feature, update an existing program object.
		Find more info here: https://learn.microsoft.com/graph/api/program-update?view=graph-rest-beta
		"""
		tags = ['programs.program']

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
		return await self.request_adapter.send_async(request_info, Program, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete program (deprecated)
		In the Microsoft Entra access reviews feature, delete a program object. Do not delete a program which still has programControl linked to it, those access reviews should first be deleted or unlinked from the program and linked to a different program.  Also, please note that the built-in default program cannot be deleted.
		Find more info here: https://learn.microsoft.com/graph/api/program-delete?view=graph-rest-beta
		"""
		tags = ['programs.program']
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



	def with_url(self, raw_url: str) -> ByProgramIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByProgramIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByProgramIdRequest(self.request_adapter, self.path_parameters)

	def controls(self,
		program_id: str,
	) -> ControlsRequest:
		if program_id is None:
			raise TypeError("program_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["program%2Did"] =  program_id

		from .controls import ControlsRequest
		return ControlsRequest(self.request_adapter, path_parameters)

