# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sections import SectionsRequest
	from .section_groups import SectionGroupsRequest
	from .resources import ResourcesRequest
	from .pages import PagesRequest
	from .operations import OperationsRequest
	from .notebooks import NotebooksRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.onenote import Onenote


class OnenoteRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/onenote"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Onenote:
		"""
		Get onenote from users
		
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
		return await self.request_adapter.send_async(request_info, Onenote, error_mapping)

	async def patch(
		self,
		body: Onenote,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Onenote:
		"""
		Update the navigation property onenote in users
		
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
		return await self.request_adapter.send_async(request_info, Onenote, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property onenote for users
		
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



	@property
	def notebooks(self,
	) -> NotebooksRequest:
		from .notebooks import NotebooksRequest
		return NotebooksRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def pages(self,
	) -> PagesRequest:
		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, self.path_parameters)

	@property
	def resources(self,
	) -> ResourcesRequest:
		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def section_groups(self,
	) -> SectionGroupsRequest:
		from .section_groups import SectionGroupsRequest
		return SectionGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def sections(self,
	) -> SectionsRequest:
		from .sections import SectionsRequest
		return SectionsRequest(self.request_adapter, self.path_parameters)

