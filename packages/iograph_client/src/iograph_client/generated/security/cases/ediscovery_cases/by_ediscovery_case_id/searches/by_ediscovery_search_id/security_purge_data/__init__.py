# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_purge_data_post_request import Security_purge_dataPostRequest


class SecurityPurgeDataRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/searches/{ediscoverySearch%2Did}/microsoft.graph.security.purgeData"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Security_purge_dataPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action purgeData
		Delete Exchange mailbox items or Microsoft Teams messages contained in an eDiscovery search. You can collect and purge the following categories of Teams content:
- Teams 1:1 chats - Chat messages, posts, and attachments shared in a Teams conversation between two people. Teams 1:1 chats are also called *conversations*.
- Teams group chats - Chat messages, posts, and attachments shared in a Teams conversation between three or more people. Also called *1:N* chats or *group conversations*.
- Teams channels - Chat messages, posts, replies, and attachments shared in a standard Teams channel.
- Private channels - Message posts, replies, and attachments shared in a private Teams channel.
- Shared channels - Message posts, replies, and attachments shared in a shared Teams channel. For more information about purging Teams messages, see:
- eDiscovery solution series: Data spillage scenario - Search and purge
- eDiscovery (Premium) workflow for content in Microsoft Teams 
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverysearch-purgedata?view=graph-rest-1.0
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


