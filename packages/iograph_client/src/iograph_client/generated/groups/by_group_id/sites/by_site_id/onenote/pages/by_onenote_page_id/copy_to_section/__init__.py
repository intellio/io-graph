# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.onenote_operation import OnenoteOperation
from iograph_models.models.copy_to_section_post_request import Copy_to_sectionPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CopyToSectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/onenote/pages/{onenotePage%2Did}/copyToSection", path_parameters)

	async def post(
		self,
		body: Copy_to_sectionPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenoteOperation:
		"""
		Invoke action copyToSection
		Copy a page to a specific section. For copy operations, you follow an asynchronous calling pattern:  First call the Copy action, and then poll the operation endpoint for the result.
		Find more info here: https://learn.microsoft.com/graph/api/page-copytosection?view=graph-rest-1.0
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, OnenoteOperation, error_mapping)


	def with_url(self, raw_url: str) -> CopyToSectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CopyToSectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CopyToSectionRequest(self.request_adapter, self.path_parameters)

