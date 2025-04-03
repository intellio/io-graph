# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parent_section_group import ParentSectionGroupRequest
	from .parent_notebook import ParentNotebookRequest
	from .pages import PagesRequest
	from .copy_to_section_group import CopyToSectionGroupRequest
	from .copy_to_notebook import CopyToNotebookRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.onenote_section import OnenoteSection


class ByOnenoteSectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/onenote/sectionGroups/{sectionGroup%2Did}/sections/{onenoteSection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnenoteSection:
		"""
		Get sections from me
		The sections in the section group. Read-only. Nullable.
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenoteSection, error_mapping)

	async def patch(
		self,
		body: OnenoteSection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenoteSection:
		"""
		Update the navigation property sections in me
		
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenoteSection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sections for me
		
		"""
		tags = ['me.onenote']
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



	def with_url(self, raw_url: str) -> ByOnenoteSectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOnenoteSectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOnenoteSectionIdRequest(self.request_adapter, self.path_parameters)

	def copy_to_notebook(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> CopyToNotebookRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .copy_to_notebook import CopyToNotebookRequest
		return CopyToNotebookRequest(self.request_adapter, path_parameters)

	def copy_to_section_group(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> CopyToSectionGroupRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .copy_to_section_group import CopyToSectionGroupRequest
		return CopyToSectionGroupRequest(self.request_adapter, path_parameters)

	def pages(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> PagesRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, path_parameters)

	def parent_notebook(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> ParentNotebookRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .parent_notebook import ParentNotebookRequest
		return ParentNotebookRequest(self.request_adapter, path_parameters)

	def parent_section_group(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> ParentSectionGroupRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .parent_section_group import ParentSectionGroupRequest
		return ParentSectionGroupRequest(self.request_adapter, path_parameters)

