# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .knowledge_base_article import KnowledgeBaseArticleRequest
	from .catalog_entry import CatalogEntryRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.windows_updates_product_revision import WindowsUpdatesProductRevision


class ByProductRevisionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/products/{product%2Did}/revisions/{productRevision%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesProductRevision:
		"""
		Get revisions from admin
		Represents a product revision.
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesProductRevision, error_mapping)

	async def patch(
		self,
		body: WindowsUpdatesProductRevision,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesProductRevision:
		"""
		Update the navigation property revisions in admin
		
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesProductRevision, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property revisions for admin
		
		"""
		tags = ['admin.adminWindows']
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



	def with_url(self, raw_url: str) -> ByProductRevisionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByProductRevisionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByProductRevisionIdRequest(self.request_adapter, self.path_parameters)

	def catalog_entry(self,
		product_id: str,
		productRevision_id: str,
	) -> CatalogEntryRequest:
		if product_id is None:
			raise TypeError("product_id cannot be null.")
		if productRevision_id is None:
			raise TypeError("productRevision_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["product%2Did"] =  product_id
		path_parameters["productRevision%2Did"] =  productRevision_id

		from .catalog_entry import CatalogEntryRequest
		return CatalogEntryRequest(self.request_adapter, path_parameters)

	def knowledge_base_article(self,
		product_id: str,
		productRevision_id: str,
	) -> KnowledgeBaseArticleRequest:
		if product_id is None:
			raise TypeError("product_id cannot be null.")
		if productRevision_id is None:
			raise TypeError("productRevision_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["product%2Did"] =  product_id
		path_parameters["productRevision%2Did"] =  productRevision_id

		from .knowledge_base_article import KnowledgeBaseArticleRequest
		return KnowledgeBaseArticleRequest(self.request_adapter, path_parameters)

