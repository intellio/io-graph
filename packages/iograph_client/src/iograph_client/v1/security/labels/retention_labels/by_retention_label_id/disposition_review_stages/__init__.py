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
	from .by_disposition_review_stage_stage_number import ByDispositionReviewStageStageNumberRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_disposition_review_stage_collection_response import SecurityDispositionReviewStageCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.security_disposition_review_stage import SecurityDispositionReviewStage


class DispositionReviewStagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/labels/retentionLabels/{retentionLabel%2Did}/dispositionReviewStages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityDispositionReviewStageCollectionResponse:
		"""
		Get dispositionReviewStages from security
		When action at the end of retention is chosen as 'dispositionReview', dispositionReviewStages specifies a sequential set of stages with at least one reviewer in each stage.
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityDispositionReviewStageCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityDispositionReviewStage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityDispositionReviewStage:
		"""
		Create new navigation property to dispositionReviewStages for security
		
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityDispositionReviewStage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DispositionReviewStagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DispositionReviewStagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DispositionReviewStagesRequest(self.request_adapter, self.path_parameters)

	def by_disposition_review_stage_stage_number(self,
		retentionLabel_id: str,
		dispositionReviewStage_stageNumber: str,
	) -> ByDispositionReviewStageStageNumberRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")
		if dispositionReviewStage_stageNumber is None:
			raise TypeError("dispositionReviewStage_stageNumber cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id
		path_parameters["dispositionReviewStage%2DstageNumber"] =  dispositionReviewStage_stageNumber

		from .by_disposition_review_stage_stage_number import ByDispositionReviewStageStageNumberRequest
		return ByDispositionReviewStageStageNumberRequest(self.request_adapter, path_parameters)

	def count(self,
		retentionLabel_id: str,
	) -> CountRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

