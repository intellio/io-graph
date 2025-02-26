# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..............request_adapter import HttpxRequestAdapter
from iograph_models.models.onenote_operation import OnenoteOperation
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.copy_to_section_post_request import Copy_to_sectionPostRequest


class CopyToSectionRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/groups/{group%2Did}/onenote/notebooks/{notebook%2Did}/sectionGroups/{sectionGroup%2Did}/sections/{onenoteSection%2Did}/pages/{onenotePage%2Did}/copyToSection"
		self.path_parameters: dict[str, Any] = path_parameters

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
		tags = ['groups.onenote']

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


