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
	from .sections import SectionsRequest
	from .section_groups import SectionGroupsRequest
	from .parent_section_group import ParentSectionGroupRequest
	from .parent_notebook import ParentNotebookRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.section_group import SectionGroup


class BySectionGroupIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onenote/sectionGroups/{sectionGroup%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SectionGroup:
		"""
		Get sectionGroups from users
		The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
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
		return await self.request_adapter.send_async(request_info, SectionGroup, error_mapping)

	async def patch(
		self,
		body: SectionGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SectionGroup:
		"""
		Update the navigation property sectionGroups in users
		
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
		return await self.request_adapter.send_async(request_info, SectionGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sectionGroups for users
		
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



	def with_url(self, raw_url: str) -> BySectionGroupIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySectionGroupIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySectionGroupIdRequest(self.request_adapter, self.path_parameters)

	def parent_notebook(self,
		user_id: str,
		sectionGroup_id: str,
	) -> ParentNotebookRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id

		from .parent_notebook import ParentNotebookRequest
		return ParentNotebookRequest(self.request_adapter, path_parameters)

	def parent_section_group(self,
		user_id: str,
		sectionGroup_id: str,
	) -> ParentSectionGroupRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id

		from .parent_section_group import ParentSectionGroupRequest
		return ParentSectionGroupRequest(self.request_adapter, path_parameters)

	def section_groups(self,
		user_id: str,
		sectionGroup_id: str,
	) -> SectionGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id

		from .section_groups import SectionGroupsRequest
		return SectionGroupsRequest(self.request_adapter, path_parameters)

	def sections(self,
		user_id: str,
		sectionGroup_id: str,
	) -> SectionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id

		from .sections import SectionsRequest
		return SectionsRequest(self.request_adapter, path_parameters)

