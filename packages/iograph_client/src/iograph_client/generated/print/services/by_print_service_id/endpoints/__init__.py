# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_print_service_endpoint_id import ByPrintServiceEndpointIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.print_service_endpoint import PrintServiceEndpoint
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.print_service_endpoint_collection_response import PrintServiceEndpointCollectionResponse


class EndpointsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/print/services/{printService%2Did}/endpoints"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintServiceEndpointCollectionResponse:
		"""
		List endpoints
		Retrieve a list of endpoints exposed by a print service.
		Find more info here: https://learn.microsoft.com/graph/api/printservice-list-endpoints?view=graph-rest-1.0
		"""
		tags = ['print.printService']

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
		return await self.request_adapter.send_async(request_info, PrintServiceEndpointCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintServiceEndpoint,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintServiceEndpoint:
		"""
		Create new navigation property to endpoints for print
		
		"""
		tags = ['print.printService']

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
		return await self.request_adapter.send_async(request_info, PrintServiceEndpoint, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_print_service_endpoint_id(self,
		printService_id: str,
		printServiceEndpoint_id: str,
	) -> ByPrintServiceEndpointIdRequest:
		if printService_id is None:
			raise TypeError("printService_id cannot be null.")
		if printServiceEndpoint_id is None:
			raise TypeError("printServiceEndpoint_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printService%2Did"] =  printService_id
		path_parameters["printServiceEndpoint%2Did"] =  printServiceEndpoint_id

		from .by_print_service_endpoint_id import ByPrintServiceEndpointIdRequest
		return ByPrintServiceEndpointIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

