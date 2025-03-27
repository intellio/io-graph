# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_message_id import ByMessageIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.message_collection_response import MessageCollectionResponse
from iograph_models.v1.message import Message


class MessagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/mailFolders/{mailFolder%2Did}/messages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MessageCollectionResponse:
		"""
		List messages
		Get all the messages in the specified user's mailbox, or those messages in a specified folder in the mailbox.
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-list-messages?view=graph-rest-1.0
		"""
		tags = ['me.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MessageCollectionResponse, error_mapping)

	async def post(
		self,
		body: Message,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Message:
		"""
		Create message in a mailfolder
		Use this API to create a new Message in a mailfolder.
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-post-messages?view=graph-rest-1.0
		"""
		tags = ['me.mailFolder']

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
		return await self.request_adapter.send_async(request_info, Message, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MessagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MessagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MessagesRequest(self.request_adapter, self.path_parameters)

	def by_message_id(self,
		mailFolder_id: str,
		message_id: str,
	) -> ByMessageIdRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["message%2Did"] =  message_id

		from .by_message_id import ByMessageIdRequest
		return ByMessageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		mailFolder_id: str,
	) -> CountRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		mailFolder_id: str,
	) -> DeltaRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

