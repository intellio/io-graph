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
	from .sections import SectionsRequest
	from .section_groups import SectionGroupsRequest
	from .resources import ResourcesRequest
	from .pages import PagesRequest
	from .operations import OperationsRequest
	from .notebooks import NotebooksRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.onenote import Onenote
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class OnenoteRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onenote", path_parameters)

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



	def with_url(self, raw_url: str) -> OnenoteRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OnenoteRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OnenoteRequest(self.request_adapter, self.path_parameters)

	def notebooks(self,
		user_id: str,
	) -> NotebooksRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .notebooks import NotebooksRequest
		return NotebooksRequest(self.request_adapter, path_parameters)

	def operations(self,
		user_id: str,
	) -> OperationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def pages(self,
		user_id: str,
	) -> PagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, path_parameters)

	def resources(self,
		user_id: str,
	) -> ResourcesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, path_parameters)

	def section_groups(self,
		user_id: str,
	) -> SectionGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .section_groups import SectionGroupsRequest
		return SectionGroupsRequest(self.request_adapter, path_parameters)

	def sections(self,
		user_id: str,
	) -> SectionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .sections import SectionsRequest
		return SectionsRequest(self.request_adapter, path_parameters)

