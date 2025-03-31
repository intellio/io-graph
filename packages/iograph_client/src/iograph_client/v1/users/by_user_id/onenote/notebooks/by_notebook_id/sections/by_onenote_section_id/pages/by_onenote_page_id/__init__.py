# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parent_section import ParentSectionRequest
	from .parent_notebook import ParentNotebookRequest
	from .preview import PreviewRequest
	from .onenote_patch_content import OnenotePatchContentRequest
	from .copy_to_section import CopyToSectionRequest
	from .content import ContentRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.v1.onenote_page import OnenotePage
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByOnenotePageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onenote/notebooks/{notebook%2Did}/sections/{onenoteSection%2Did}/pages/{onenotePage%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnenotePage:
		"""
		Get pages from users
		The collection of pages in the section.  Read-only. Nullable.
		"""
		tags = ['users.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)

	async def patch(
		self,
		body: OnenotePage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenotePage:
		"""
		Update the navigation property pages in users
		
		"""
		tags = ['users.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property pages for users
		
		"""
		tags = ['users.onenote']
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



	def with_url(self, raw_url: str) -> ByOnenotePageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOnenotePageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOnenotePageIdRequest(self.request_adapter, self.path_parameters)

	def content(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> ContentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

	def copy_to_section(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> CopyToSectionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .copy_to_section import CopyToSectionRequest
		return CopyToSectionRequest(self.request_adapter, path_parameters)

	def onenote_patch_content(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> OnenotePatchContentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .onenote_patch_content import OnenotePatchContentRequest
		return OnenotePatchContentRequest(self.request_adapter, path_parameters)

	def preview(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> PreviewRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .preview import PreviewRequest
		return PreviewRequest(self.request_adapter, path_parameters)

	def parent_notebook(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> ParentNotebookRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .parent_notebook import ParentNotebookRequest
		return ParentNotebookRequest(self.request_adapter, path_parameters)

	def parent_section(self,
		user_id: str,
		notebook_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> ParentSectionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["notebook%2Did"] =  notebook_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .parent_section import ParentSectionRequest
		return ParentSectionRequest(self.request_adapter, path_parameters)

