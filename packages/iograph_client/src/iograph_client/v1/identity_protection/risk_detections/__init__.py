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
	from .count import CountRequest
	from .by_risk_detection_id import ByRiskDetectionIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.risk_detection_collection_response import RiskDetectionCollectionResponse
from iograph_models.v1.risk_detection import RiskDetection
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class RiskDetectionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityProtection/riskDetections", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RiskDetectionCollectionResponse:
		"""
		List riskDetections
		Get a list of the riskDetection objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/riskdetection-list?view=graph-rest-1.0
		"""
		tags = ['identityProtection.riskDetection']

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
		return await self.request_adapter.send_async(request_info, RiskDetectionCollectionResponse, error_mapping)

	async def post(
		self,
		body: RiskDetection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RiskDetection:
		"""
		Create new navigation property to riskDetections for identityProtection
		
		"""
		tags = ['identityProtection.riskDetection']

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
		return await self.request_adapter.send_async(request_info, RiskDetection, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RiskDetectionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RiskDetectionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RiskDetectionsRequest(self.request_adapter, self.path_parameters)

	def by_risk_detection_id(self,
		riskDetection_id: str,
	) -> ByRiskDetectionIdRequest:
		if riskDetection_id is None:
			raise TypeError("riskDetection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["riskDetection%2Did"] =  riskDetection_id

		from .by_risk_detection_id import ByRiskDetectionIdRequest
		return ByRiskDetectionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

