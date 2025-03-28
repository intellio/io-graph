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
	from .by_reference_definition_id import ByReferenceDefinitionIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.industry_data_reference_definition import IndustryDataReferenceDefinition
from iograph_models.beta.industry_data_reference_definition_collection_response import IndustryDataReferenceDefinitionCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ReferenceDefinitionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/industryData/referenceDefinitions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IndustryDataReferenceDefinitionCollectionResponse:
		"""
		List referenceDefinitions
		Get a list of the referenceDefinition objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/industrydata-referencedefinition-list?view=graph-rest-beta
		"""
		tags = ['external.industryDataRoot']

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
		return await self.request_adapter.send_async(request_info, IndustryDataReferenceDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: IndustryDataReferenceDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IndustryDataReferenceDefinition:
		"""
		Create referenceDefinition
		Create a new referenceDefinition object. referenceDefinition objects associate incoming data with standardized reference types values for validation. You can extend the following reference types with other codes that better align with your source data.
		Find more info here: https://learn.microsoft.com/graph/api/industrydata-referencedefinition-post?view=graph-rest-beta
		"""
		tags = ['external.industryDataRoot']

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
		return await self.request_adapter.send_async(request_info, IndustryDataReferenceDefinition, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReferenceDefinitionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReferenceDefinitionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReferenceDefinitionsRequest(self.request_adapter, self.path_parameters)

	def by_reference_definition_id(self,
		referenceDefinition_id: str,
	) -> ByReferenceDefinitionIdRequest:
		if referenceDefinition_id is None:
			raise TypeError("referenceDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["referenceDefinition%2Did"] =  referenceDefinition_id

		from .by_reference_definition_id import ByReferenceDefinitionIdRequest
		return ByReferenceDefinitionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

