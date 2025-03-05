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
	from .copy_notebook import CopyNotebookRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.notebook import Notebook


class ByNotebookIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/onenote/notebooks/{notebook%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Notebook:
		"""
		Get notebooks from groups
		The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.
		"""
		tags = ['groups.onenote']

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
		return await self.request_adapter.send_async(request_info, Notebook, error_mapping)

	async def patch(
		self,
		body: Notebook,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Notebook:
		"""
		Update the navigation property notebooks in groups
		
		"""
		tags = ['groups.onenote']

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
		return await self.request_adapter.send_async(request_info, Notebook, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property notebooks for groups
		
		"""
		tags = ['groups.onenote']
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



	def with_url(self, raw_url: str) -> ByNotebookIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByNotebookIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByNotebookIdRequest(self.request_adapter, self.path_parameters)

	def copy_notebook(self,
		group_id: str,
		notebook_id: str,
	) -> CopyNotebookRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["notebook%2Did"] =  notebook_id

		from .copy_notebook import CopyNotebookRequest
		return CopyNotebookRequest(self.request_adapter, path_parameters)

	def section_groups(self,
		group_id: str,
		notebook_id: str,
	) -> SectionGroupsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["notebook%2Did"] =  notebook_id

		from .section_groups import SectionGroupsRequest
		return SectionGroupsRequest(self.request_adapter, path_parameters)

	def sections(self,
		group_id: str,
		notebook_id: str,
	) -> SectionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["notebook%2Did"] =  notebook_id

		from .sections import SectionsRequest
		return SectionsRequest(self.request_adapter, path_parameters)

