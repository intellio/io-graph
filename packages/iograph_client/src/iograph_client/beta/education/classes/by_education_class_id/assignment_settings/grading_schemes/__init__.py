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
	from .by_education_grading_scheme_id import ByEducationGradingSchemeIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.education_grading_scheme import EducationGradingScheme
from iograph_models.beta.education_grading_scheme_collection_response import EducationGradingSchemeCollectionResponse


class GradingSchemesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignmentSettings/gradingSchemes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationGradingSchemeCollectionResponse:
		"""
		Get educationGradingScheme
		Read the properties and relationships of an educationGradingScheme object.
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
		return await self.request_adapter.send_async(request_info, EducationGradingSchemeCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationGradingScheme,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationGradingScheme:
		"""
		Create educationGradingScheme
		Create a new educationGradingScheme object.
		Find more info here: https://learn.microsoft.com/graph/api/educationgradingscheme-post?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EducationGradingScheme, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> GradingSchemesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GradingSchemesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GradingSchemesRequest(self.request_adapter, self.path_parameters)

	def by_education_grading_scheme_id(self,
		educationClass_id: str,
		educationGradingScheme_id: str,
	) -> ByEducationGradingSchemeIdRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationGradingScheme_id is None:
			raise TypeError("educationGradingScheme_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationGradingScheme%2Did"] =  educationGradingScheme_id

		from .by_education_grading_scheme_id import ByEducationGradingSchemeIdRequest
		return ByEducationGradingSchemeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		educationClass_id: str,
	) -> CountRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

