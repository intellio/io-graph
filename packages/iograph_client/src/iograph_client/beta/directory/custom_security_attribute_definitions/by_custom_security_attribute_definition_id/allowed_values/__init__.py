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
	from .by_allowed_value_id import ByAllowedValueIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.allowed_value import AllowedValue
from iograph_models.beta.allowed_value_collection_response import AllowedValueCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AllowedValuesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/customSecurityAttributeDefinitions/{customSecurityAttributeDefinition%2Did}/allowedValues", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AllowedValueCollectionResponse:
		"""
		List allowedValues
		Get a list of the allowedValue objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/customsecurityattributedefinition-list-allowedvalues?view=graph-rest-beta
		"""
		tags = ['directory.customSecurityAttributeDefinition']

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
		return await self.request_adapter.send_async(request_info, AllowedValueCollectionResponse, error_mapping)

	async def post(
		self,
		body: AllowedValue,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AllowedValue:
		"""
		Create allowedValue
		Create a new allowedValue object.
		Find more info here: https://learn.microsoft.com/graph/api/customsecurityattributedefinition-post-allowedvalues?view=graph-rest-beta
		"""
		tags = ['directory.customSecurityAttributeDefinition']

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
		return await self.request_adapter.send_async(request_info, AllowedValue, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AllowedValuesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AllowedValuesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AllowedValuesRequest(self.request_adapter, self.path_parameters)

	def by_allowed_value_id(self,
		customSecurityAttributeDefinition_id: str,
		allowedValue_id: str,
	) -> ByAllowedValueIdRequest:
		if customSecurityAttributeDefinition_id is None:
			raise TypeError("customSecurityAttributeDefinition_id cannot be null.")
		if allowedValue_id is None:
			raise TypeError("allowedValue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["customSecurityAttributeDefinition%2Did"] =  customSecurityAttributeDefinition_id
		path_parameters["allowedValue%2Did"] =  allowedValue_id

		from .by_allowed_value_id import ByAllowedValueIdRequest
		return ByAllowedValueIdRequest(self.request_adapter, path_parameters)

	def count(self,
		customSecurityAttributeDefinition_id: str,
	) -> CountRequest:
		if customSecurityAttributeDefinition_id is None:
			raise TypeError("customSecurityAttributeDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["customSecurityAttributeDefinition%2Did"] =  customSecurityAttributeDefinition_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

