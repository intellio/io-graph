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
	from .count import CountRequest
	from .by_program_control_id import ByProgramControlIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.program_control_collection_response import ProgramControlCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.program_control import ProgramControl


class ControlsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/programs/{program%2Did}/controls", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ProgramControlCollectionResponse:
		"""
		List programControls of a program (deprecated)
		In the Microsoft Entra access reviews feature, list all the programControl objects, linked to a particular program.
		Find more info here: https://learn.microsoft.com/graph/api/program-listcontrols?view=graph-rest-beta
		"""
		tags = ['programs.programControl']

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
		return await self.request_adapter.send_async(request_info, ProgramControlCollectionResponse, error_mapping)

	async def post(
		self,
		body: ProgramControl,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ProgramControl:
		"""
		Create new navigation property to controls for programs
		
		"""
		tags = ['programs.programControl']

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
		return await self.request_adapter.send_async(request_info, ProgramControl, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ControlsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ControlsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ControlsRequest(self.request_adapter, self.path_parameters)

	def by_program_control_id(self,
		program_id: str,
		programControl_id: str,
	) -> ByProgramControlIdRequest:
		if program_id is None:
			raise TypeError("program_id cannot be null.")
		if programControl_id is None:
			raise TypeError("programControl_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["program%2Did"] =  program_id
		path_parameters["programControl%2Did"] =  programControl_id

		from .by_program_control_id import ByProgramControlIdRequest
		return ByProgramControlIdRequest(self.request_adapter, path_parameters)

	def count(self,
		program_id: str,
	) -> CountRequest:
		if program_id is None:
			raise TypeError("program_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["program%2Did"] =  program_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

