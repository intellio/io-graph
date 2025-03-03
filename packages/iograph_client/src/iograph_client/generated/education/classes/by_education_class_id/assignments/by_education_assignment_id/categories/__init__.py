# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .ref import RefRequest
	from .count import CountRequest
	from .by_education_category_id import ByEducationCategoryIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.education_category import EducationCategory
from iograph_models.models.education_category_collection_response import EducationCategoryCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CategoriesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/categories", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationCategoryCollectionResponse:
		"""
		List categories
		List all the categories associated with an assignment. Only teachers, students, and applications with application permissions can perform this operation.
		Find more info here: https://learn.microsoft.com/graph/api/educationassignment-list-categories?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationCategoryCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationCategory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationCategory:
		"""
		Create educationCategories
		Add one or more existing educationCategory objects to the specified  educationAssignment. Only teachers can perform this operation.
		Find more info here: https://learn.microsoft.com/graph/api/educationassignment-post-categories?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationCategory, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CategoriesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CategoriesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def by_education_category_id(self,
	) -> ByEducationCategoryIdRequest:
		from .by_education_category_id import ByEducationCategoryIdRequest
		return ByEducationCategoryIdRequest(self.request_adapter, self.path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def ref(self,
	) -> RefRequest:
		from .ref import RefRequest
		return RefRequest(self.request_adapter, self.path_parameters)

