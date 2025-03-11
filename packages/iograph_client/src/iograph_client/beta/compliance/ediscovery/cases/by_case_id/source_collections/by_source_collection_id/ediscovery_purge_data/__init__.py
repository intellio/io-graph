# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class EdiscoveryPurgeDataRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/sourceCollections/{sourceCollection%2Did}/microsoft.graph.ediscovery.purgeData", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action purgeData
		Permanently delete Microsoft Teams messages contained in a sourceCollection. You can collect and purge the following categories of Teams content:
- Teams 1:1 chats - Chat messages, posts, and attachments shared in a Teams conversation between two people. Teams 1:1 chats are also called *conversations*.
- Teams group chats - Chat messages, posts, and attachments shared in a Teams conversation between three or more people. Also called *1:N* chats or *group conversations*.
- Teams channels - Chat messages, posts, replies, and attachments shared in a standard Teams channel.
- Private channels - Message posts, replies, and attachments shared in a private Teams channel.
- Shared channels - Message posts, replies, and attachments shared in a shared Teams channel. For more information about purging Teams messages, see:
- eDiscovery solution series: Data spillage scenario - Search and purge
- Advanced eDiscovery workflow for content in Microsoft Teams 
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-sourcecollection-purgedata?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> EdiscoveryPurgeDataRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EdiscoveryPurgeDataRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EdiscoveryPurgeDataRequest(self.request_adapter, self.path_parameters)

