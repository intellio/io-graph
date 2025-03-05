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
	from .count import CountRequest
	from .by_landing_page_detail_id import ByLandingPageDetailIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.landing_page_detail_collection_response import LandingPageDetailCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.landing_page_detail import LandingPageDetail


class DetailsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/attackSimulation/landingPages/{landingPage%2Did}/details", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LandingPageDetailCollectionResponse:
		"""
		Get details from security
		The detail information for a landing page associated with a simulation during its creation.
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, LandingPageDetailCollectionResponse, error_mapping)

	async def post(
		self,
		body: LandingPageDetail,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LandingPageDetail:
		"""
		Create new navigation property to details for security
		
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, LandingPageDetail, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DetailsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DetailsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DetailsRequest(self.request_adapter, self.path_parameters)

	def by_landing_page_detail_id(self,
		landingPage_id: str,
		landingPageDetail_id: str,
	) -> ByLandingPageDetailIdRequest:
		if landingPage_id is None:
			raise TypeError("landingPage_id cannot be null.")
		if landingPageDetail_id is None:
			raise TypeError("landingPageDetail_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["landingPage%2Did"] =  landingPage_id
		path_parameters["landingPageDetail%2Did"] =  landingPageDetail_id

		from .by_landing_page_detail_id import ByLandingPageDetailIdRequest
		return ByLandingPageDetailIdRequest(self.request_adapter, path_parameters)

	def count(self,
		landingPage_id: str,
	) -> CountRequest:
		if landingPage_id is None:
			raise TypeError("landingPage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["landingPage%2Did"] =  landingPage_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

