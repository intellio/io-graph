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
	from .update_ti_indicators import UpdateTiIndicatorsRequest
	from .submit_ti_indicators import SubmitTiIndicatorsRequest
	from .delete_ti_indicators_by_external_id import DeleteTiIndicatorsByExternalIdRequest
	from .delete_ti_indicators import DeleteTiIndicatorsRequest
	from .count import CountRequest
	from .by_ti_indicator_id import ByTiIndicatorIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.ti_indicator import TiIndicator
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ti_indicator_collection_response import TiIndicatorCollectionResponse


class TiIndicatorsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/tiIndicators", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TiIndicatorCollectionResponse:
		"""
		List threat intelligence indicators
		Retrieve a list of tiIndicator objects.
		Find more info here: https://learn.microsoft.com/graph/api/tiindicators-list?view=graph-rest-beta
		"""
		tags = ['security.tiIndicator']

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
		return await self.request_adapter.send_async(request_info, TiIndicatorCollectionResponse, error_mapping)

	async def post(
		self,
		body: TiIndicator,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TiIndicator:
		"""
		Create threat intelligence indicator
		Create a new tiIndicator object.
		Find more info here: https://learn.microsoft.com/graph/api/tiindicators-post?view=graph-rest-beta
		"""
		tags = ['security.tiIndicator']

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
		return await self.request_adapter.send_async(request_info, TiIndicator, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TiIndicatorsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TiIndicatorsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TiIndicatorsRequest(self.request_adapter, self.path_parameters)

	def by_ti_indicator_id(self,
		tiIndicator_id: str,
	) -> ByTiIndicatorIdRequest:
		if tiIndicator_id is None:
			raise TypeError("tiIndicator_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["tiIndicator%2Did"] =  tiIndicator_id

		from .by_ti_indicator_id import ByTiIndicatorIdRequest
		return ByTiIndicatorIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delete_ti_indicators(self,
	) -> DeleteTiIndicatorsRequest:
		from .delete_ti_indicators import DeleteTiIndicatorsRequest
		return DeleteTiIndicatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def delete_ti_indicators_by_external_id(self,
	) -> DeleteTiIndicatorsByExternalIdRequest:
		from .delete_ti_indicators_by_external_id import DeleteTiIndicatorsByExternalIdRequest
		return DeleteTiIndicatorsByExternalIdRequest(self.request_adapter, self.path_parameters)

	@property
	def submit_ti_indicators(self,
	) -> SubmitTiIndicatorsRequest:
		from .submit_ti_indicators import SubmitTiIndicatorsRequest
		return SubmitTiIndicatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def update_ti_indicators(self,
	) -> UpdateTiIndicatorsRequest:
		from .update_ti_indicators import UpdateTiIndicatorsRequest
		return UpdateTiIndicatorsRequest(self.request_adapter, self.path_parameters)

