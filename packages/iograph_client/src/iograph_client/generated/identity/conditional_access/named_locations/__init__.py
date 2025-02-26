# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_named_location_id import ByNamedLocationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.named_location import NamedLocation
from iograph_models.models.named_location_collection_response import NamedLocationCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class NamedLocationsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/conditionalAccess/namedLocations"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NamedLocationCollectionResponse:
		"""
		List namedLocations
		Get a list of namedLocation objects.
		Find more info here: https://learn.microsoft.com/graph/api/conditionalaccessroot-list-namedlocations?view=graph-rest-1.0
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, NamedLocationCollectionResponse, error_mapping)

	async def post(
		self,
		body: NamedLocation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NamedLocation:
		"""
		Create namedLocation
		Create a new namedLocation object. Named locations can be either ipNamedLocation or countryNamedLocation objects.
		Find more info here: https://learn.microsoft.com/graph/api/conditionalaccessroot-post-namedlocations?view=graph-rest-1.0
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, NamedLocation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_named_location_id(self,
		namedLocation_id: str,
	) -> ByNamedLocationIdRequest:
		if namedLocation_id is None:
			raise TypeError("namedLocation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["namedLocation%2Did"] =  namedLocation_id

		from .by_named_location_id import ByNamedLocationIdRequest
		return ByNamedLocationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

