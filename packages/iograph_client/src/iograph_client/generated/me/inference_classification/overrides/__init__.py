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
	from .by_inference_classification_override_id import ByInferenceClassificationOverrideIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.inference_classification_override import InferenceClassificationOverride
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.inference_classification_override_collection_response import InferenceClassificationOverrideCollectionResponse


class OverridesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/inferenceClassification/overrides", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InferenceClassificationOverrideCollectionResponse:
		"""
		List overrides
		Get the overrides that a user has set up to always classify messages from certain senders in specific ways. Each override corresponds to an SMTP address of a sender. Initially, a user does not have any overrides.
		Find more info here: https://learn.microsoft.com/graph/api/inferenceclassification-list-overrides?view=graph-rest-1.0
		"""
		tags = ['me.inferenceClassification']

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
		return await self.request_adapter.send_async(request_info, InferenceClassificationOverrideCollectionResponse, error_mapping)

	async def post(
		self,
		body: InferenceClassificationOverride,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InferenceClassificationOverride:
		"""
		Create inferenceClassificationOverride
		Create an override for a sender identified by an SMTP address. Future messages from that SMTP address will be consistently classified
as specified in the override. Note
		Find more info here: https://learn.microsoft.com/graph/api/inferenceclassification-post-overrides?view=graph-rest-1.0
		"""
		tags = ['me.inferenceClassification']

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
		return await self.request_adapter.send_async(request_info, InferenceClassificationOverride, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OverridesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OverridesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OverridesRequest(self.request_adapter, self.path_parameters)

	def by_inference_classification_override_id(self,
		inferenceClassificationOverride_id: str,
	) -> ByInferenceClassificationOverrideIdRequest:
		if inferenceClassificationOverride_id is None:
			raise TypeError("inferenceClassificationOverride_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["inferenceClassificationOverride%2Did"] =  inferenceClassificationOverride_id

		from .by_inference_classification_override_id import ByInferenceClassificationOverrideIdRequest
		return ByInferenceClassificationOverrideIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

