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
	from .by_subcategory_template_id import BySubcategoryTemplateIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_subcategory_template import SecuritySubcategoryTemplate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_subcategory_template_collection_response import SecuritySubcategoryTemplateCollectionResponse


class SubcategoriesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/labels/categories/{categoryTemplate%2Did}/subcategories", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecuritySubcategoryTemplateCollectionResponse:
		"""
		List subcategories
		Get a list of subcategoryTemplate objects associated with a category template.
		Find more info here: https://learn.microsoft.com/graph/api/security-categorytemplate-list-subcategories?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, SecuritySubcategoryTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecuritySubcategoryTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecuritySubcategoryTemplate:
		"""
		Create subcategoryTemplate
		Create a new subcategoryTemplate object.
		Find more info here: https://learn.microsoft.com/graph/api/security-categorytemplate-post-subcategories?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, SecuritySubcategoryTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SubcategoriesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SubcategoriesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SubcategoriesRequest(self.request_adapter, self.path_parameters)

	def by_subcategory_template_id(self,
		categoryTemplate_id: str,
		subcategoryTemplate_id: str,
	) -> BySubcategoryTemplateIdRequest:
		if categoryTemplate_id is None:
			raise TypeError("categoryTemplate_id cannot be null.")
		if subcategoryTemplate_id is None:
			raise TypeError("subcategoryTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["categoryTemplate%2Did"] =  categoryTemplate_id
		path_parameters["subcategoryTemplate%2Did"] =  subcategoryTemplate_id

		from .by_subcategory_template_id import BySubcategoryTemplateIdRequest
		return BySubcategoryTemplateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		categoryTemplate_id: str,
	) -> CountRequest:
		if categoryTemplate_id is None:
			raise TypeError("categoryTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["categoryTemplate%2Did"] =  categoryTemplate_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

