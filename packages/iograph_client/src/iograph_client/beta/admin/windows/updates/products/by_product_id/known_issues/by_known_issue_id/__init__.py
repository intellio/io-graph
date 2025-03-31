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
	from .resolving_knowledge_base_article import ResolvingKnowledgeBaseArticleRequest
	from .originating_knowledge_base_article import OriginatingKnowledgeBaseArticleRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_known_issue import WindowsUpdatesKnownIssue
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByKnownIssueIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/products/{product%2Did}/knownIssues/{knownIssue%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesKnownIssue:
		"""
		Get knownIssues from admin
		Represents a known issue related to a Windows product.
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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesKnownIssue, error_mapping)

	async def patch(
		self,
		body: WindowsUpdatesKnownIssue,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesKnownIssue:
		"""
		Update the navigation property knownIssues in admin
		
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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesKnownIssue, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property knownIssues for admin
		
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



	def with_url(self, raw_url: str) -> ByKnownIssueIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByKnownIssueIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByKnownIssueIdRequest(self.request_adapter, self.path_parameters)

	def originating_knowledge_base_article(self,
		product_id: str,
		knownIssue_id: str,
	) -> OriginatingKnowledgeBaseArticleRequest:
		if product_id is None:
			raise TypeError("product_id cannot be null.")
		if knownIssue_id is None:
			raise TypeError("knownIssue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["product%2Did"] =  product_id
		path_parameters["knownIssue%2Did"] =  knownIssue_id

		from .originating_knowledge_base_article import OriginatingKnowledgeBaseArticleRequest
		return OriginatingKnowledgeBaseArticleRequest(self.request_adapter, path_parameters)

	def resolving_knowledge_base_article(self,
		product_id: str,
		knownIssue_id: str,
	) -> ResolvingKnowledgeBaseArticleRequest:
		if product_id is None:
			raise TypeError("product_id cannot be null.")
		if knownIssue_id is None:
			raise TypeError("knownIssue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["product%2Did"] =  product_id
		path_parameters["knownIssue%2Did"] =  knownIssue_id

		from .resolving_knowledge_base_article import ResolvingKnowledgeBaseArticleRequest
		return ResolvingKnowledgeBaseArticleRequest(self.request_adapter, path_parameters)

