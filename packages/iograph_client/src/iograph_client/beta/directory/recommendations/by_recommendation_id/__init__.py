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
	from .reactivate import ReactivateRequest
	from .postpone import PostponeRequest
	from .dismiss import DismissRequest
	from .complete import CompleteRequest
	from .impacted_resources import ImpactedResourcesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.recommendation import Recommendation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByRecommendationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/recommendations/{recommendation%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Recommendation:
		"""
		Get recommendation
		Read the properties and relationships of a recommendation object.
		Find more info here: https://learn.microsoft.com/graph/api/recommendation-get?view=graph-rest-beta
		"""
		tags = ['directory.recommendation']

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
		return await self.request_adapter.send_async(request_info, Recommendation, error_mapping)

	async def patch(
		self,
		body: Recommendation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Recommendation:
		"""
		Update the navigation property recommendations in directory
		
		"""
		tags = ['directory.recommendation']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Recommendation, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property recommendations for directory
		
		"""
		tags = ['directory.recommendation']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByRecommendationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByRecommendationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByRecommendationIdRequest(self.request_adapter, self.path_parameters)

	def impacted_resources(self,
		recommendation_id: str,
	) -> ImpactedResourcesRequest:
		if recommendation_id is None:
			raise TypeError("recommendation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["recommendation%2Did"] =  recommendation_id

		from .impacted_resources import ImpactedResourcesRequest
		return ImpactedResourcesRequest(self.request_adapter, path_parameters)

	def complete(self,
		recommendation_id: str,
	) -> CompleteRequest:
		if recommendation_id is None:
			raise TypeError("recommendation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["recommendation%2Did"] =  recommendation_id

		from .complete import CompleteRequest
		return CompleteRequest(self.request_adapter, path_parameters)

	def dismiss(self,
		recommendation_id: str,
	) -> DismissRequest:
		if recommendation_id is None:
			raise TypeError("recommendation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["recommendation%2Did"] =  recommendation_id

		from .dismiss import DismissRequest
		return DismissRequest(self.request_adapter, path_parameters)

	def postpone(self,
		recommendation_id: str,
	) -> PostponeRequest:
		if recommendation_id is None:
			raise TypeError("recommendation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["recommendation%2Did"] =  recommendation_id

		from .postpone import PostponeRequest
		return PostponeRequest(self.request_adapter, path_parameters)

	def reactivate(self,
		recommendation_id: str,
	) -> ReactivateRequest:
		if recommendation_id is None:
			raise TypeError("recommendation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["recommendation%2Did"] =  recommendation_id

		from .reactivate import ReactivateRequest
		return ReactivateRequest(self.request_adapter, path_parameters)

