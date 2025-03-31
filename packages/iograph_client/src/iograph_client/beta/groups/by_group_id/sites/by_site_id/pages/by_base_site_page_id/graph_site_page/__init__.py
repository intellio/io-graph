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
	from .web_parts import WebPartsRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .created_by_user import CreatedByUserRequest
	from .canvas_layout import CanvasLayoutRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.site_page import SitePage
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GraphSitePageRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/pages/{baseSitePage%2Did}/graph.sitePage", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SitePage:
		"""
		Get the item of type microsoft.graph.baseSitePage as microsoft.graph.sitePage
		
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, SitePage, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> GraphSitePageRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphSitePageRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphSitePageRequest(self.request_adapter, self.path_parameters)

	def canvas_layout(self,
		group_id: str,
		site_id: str,
		baseSitePage_id: str,
	) -> CanvasLayoutRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id

		from .canvas_layout import CanvasLayoutRequest
		return CanvasLayoutRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		group_id: str,
		site_id: str,
		baseSitePage_id: str,
	) -> CreatedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		group_id: str,
		site_id: str,
		baseSitePage_id: str,
	) -> LastModifiedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def web_parts(self,
		group_id: str,
		site_id: str,
		baseSitePage_id: str,
	) -> WebPartsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id

		from .web_parts import WebPartsRequest
		return WebPartsRequest(self.request_adapter, path_parameters)

