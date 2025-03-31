# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_mailbox_item_id import ByMailboxItemIdRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.mailbox_item_collection_response import MailboxItemCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ItemsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/exchange/mailboxes/{mailbox%2Did}/folders/{mailboxFolder%2Did}/childFolders/{mailboxFolder%2Did1}/items", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxItemCollectionResponse:
		"""
		Get items from admin
		The collection of items in this folder.
		"""
		tags = ['admin.exchangeAdmin']

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
		return await self.request_adapter.send_async(request_info, MailboxItemCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ItemsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemsRequest(self.request_adapter, self.path_parameters)

	def by_mailbox_item_id(self,
		mailbox_id: str,
		mailboxFolder_id: str,
		mailboxFolder_id1: str,
		mailboxItem_id: str,
	) -> ByMailboxItemIdRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")
		if mailboxFolder_id is None:
			raise TypeError("mailboxFolder_id cannot be null.")
		if mailboxFolder_id1 is None:
			raise TypeError("mailboxFolder_id1 cannot be null.")
		if mailboxItem_id is None:
			raise TypeError("mailboxItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id
		path_parameters["mailboxFolder%2Did"] =  mailboxFolder_id
		path_parameters["mailboxFolder%2Did1"] =  mailboxFolder_id1
		path_parameters["mailboxItem%2Did"] =  mailboxItem_id

		from .by_mailbox_item_id import ByMailboxItemIdRequest
		return ByMailboxItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		mailbox_id: str,
		mailboxFolder_id: str,
		mailboxFolder_id1: str,
	) -> CountRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")
		if mailboxFolder_id is None:
			raise TypeError("mailboxFolder_id cannot be null.")
		if mailboxFolder_id1 is None:
			raise TypeError("mailboxFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id
		path_parameters["mailboxFolder%2Did"] =  mailboxFolder_id
		path_parameters["mailboxFolder%2Did1"] =  mailboxFolder_id1

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		mailbox_id: str,
		mailboxFolder_id: str,
		mailboxFolder_id1: str,
	) -> DeltaRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")
		if mailboxFolder_id is None:
			raise TypeError("mailboxFolder_id cannot be null.")
		if mailboxFolder_id1 is None:
			raise TypeError("mailboxFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id
		path_parameters["mailboxFolder%2Did"] =  mailboxFolder_id
		path_parameters["mailboxFolder%2Did1"] =  mailboxFolder_id1

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

