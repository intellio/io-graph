# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_learning_content_id import ByLearningContentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.learning_content_collection_response import LearningContentCollectionResponse
from iograph_models.v1.learning_content import LearningContent


class LearningContentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}/learningContents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LearningContentCollectionResponse:
		"""
		List learningContents
		Get a list of the learningContent resources and their properties. This list represents the metadata of the specified provider's content in Viva Learning.
		Find more info here: https://learn.microsoft.com/graph/api/learningprovider-list-learningcontents?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.learningProvider']

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
		return await self.request_adapter.send_async(request_info, LearningContentCollectionResponse, error_mapping)

	async def post(
		self,
		body: LearningContent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LearningContent:
		"""
		Create new navigation property to learningContents for employeeExperience
		
		"""
		tags = ['employeeExperience.learningProvider']

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
		return await self.request_adapter.send_async(request_info, LearningContent, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LearningContentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LearningContentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LearningContentsRequest(self.request_adapter, self.path_parameters)

	def by_learning_content_id(self,
		learningProvider_id: str,
		learningContent_id: str,
	) -> ByLearningContentIdRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")
		if learningContent_id is None:
			raise TypeError("learningContent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id
		path_parameters["learningContent%2Did"] =  learningContent_id

		from .by_learning_content_id import ByLearningContentIdRequest
		return ByLearningContentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		learningProvider_id: str,
	) -> CountRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

