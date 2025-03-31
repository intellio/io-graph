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
	from .get_recent_notebooks_with_includepersonalnotebooks import GetRecentNotebooksWithIncludePersonalNotebooksRequest
	from .get_notebook_from_web_url import GetNotebookFromWebUrlRequest
	from .count import CountRequest
	from .by_notebook_id import ByNotebookIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.notebook_collection_response import NotebookCollectionResponse
from iograph_models.v1.notebook import Notebook


class NotebooksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/onenote/notebooks", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NotebookCollectionResponse:
		"""
		List notebooks
		Retrieve a list of notebook objects.
		Find more info here: https://learn.microsoft.com/graph/api/onenote-list-notebooks?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, NotebookCollectionResponse, error_mapping)

	async def post(
		self,
		body: Notebook,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Notebook:
		"""
		Create notebook
		Create a new OneNote notebook.
		Find more info here: https://learn.microsoft.com/graph/api/onenote-post-notebooks?view=graph-rest-1.0
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, Notebook, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> NotebooksRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NotebooksRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NotebooksRequest(self.request_adapter, self.path_parameters)

	def by_notebook_id(self,
		notebook_id: str,
	) -> ByNotebookIdRequest:
		if notebook_id is None:
			raise TypeError("notebook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["notebook%2Did"] =  notebook_id

		from .by_notebook_id import ByNotebookIdRequest
		return ByNotebookIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def get_notebook_from_web_url(self,
	) -> GetNotebookFromWebUrlRequest:
		from .get_notebook_from_web_url import GetNotebookFromWebUrlRequest
		return GetNotebookFromWebUrlRequest(self.request_adapter, self.path_parameters)

	def get_recent_notebooks_with_includepersonalnotebooks(self,
		includePersonalNotebooks: bool,
	) -> GetRecentNotebooksWithIncludePersonalNotebooksRequest:
		if includePersonalNotebooks is None:
			raise TypeError("includePersonalNotebooks cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["includePersonalNotebooks"] =  includePersonalNotebooks

		from .get_recent_notebooks_with_includepersonalnotebooks import GetRecentNotebooksWithIncludePersonalNotebooksRequest
		return GetRecentNotebooksWithIncludePersonalNotebooksRequest(self.request_adapter, path_parameters)

