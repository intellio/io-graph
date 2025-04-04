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
	from .by_learning_provider_id import ByLearningProviderIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.learning_provider_collection_response import LearningProviderCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.learning_provider import LearningProvider


class LearningProvidersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LearningProviderCollectionResponse:
		"""
		List learningProviders
		Get a list of the learningProvider resources registered in Viva Learning for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/employeeexperience-list-learningproviders?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, LearningProviderCollectionResponse, error_mapping)

	async def post(
		self,
		body: LearningProvider,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LearningProvider:
		"""
		Create learningProvider
		Create a new learningProvider object and register it with Viva Learning using the specified display name and logos for different themes.
		Find more info here: https://learn.microsoft.com/graph/api/employeeexperience-post-learningproviders?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, LearningProvider, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LearningProvidersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LearningProvidersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LearningProvidersRequest(self.request_adapter, self.path_parameters)

	def by_learning_provider_id(self,
		learningProvider_id: str,
	) -> ByLearningProviderIdRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id

		from .by_learning_provider_id import ByLearningProviderIdRequest
		return ByLearningProviderIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

