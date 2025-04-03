# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_message_recipient_id import ByMessageRecipientIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.message_recipient import MessageRecipient
from iograph_models.beta.message_recipient_collection_response import MessageRecipientCollectionResponse


class RecipientsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/exchange/messageTraces/{messageTrace%2Did}/recipients", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MessageRecipientCollectionResponse:
		"""
		Get recipients from admin
		
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
		return await self.request_adapter.send_async(request_info, MessageRecipientCollectionResponse, error_mapping)

	async def post(
		self,
		body: MessageRecipient,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MessageRecipient:
		"""
		Create new navigation property to recipients for admin
		
		"""
		tags = ['admin.exchangeAdmin']

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
		return await self.request_adapter.send_async(request_info, MessageRecipient, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RecipientsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RecipientsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RecipientsRequest(self.request_adapter, self.path_parameters)

	def by_message_recipient_id(self,
		messageTrace_id: str,
		messageRecipient_id: str,
	) -> ByMessageRecipientIdRequest:
		if messageTrace_id is None:
			raise TypeError("messageTrace_id cannot be null.")
		if messageRecipient_id is None:
			raise TypeError("messageRecipient_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["messageTrace%2Did"] =  messageTrace_id
		path_parameters["messageRecipient%2Did"] =  messageRecipient_id

		from .by_message_recipient_id import ByMessageRecipientIdRequest
		return ByMessageRecipientIdRequest(self.request_adapter, path_parameters)

	def count(self,
		messageTrace_id: str,
	) -> CountRequest:
		if messageTrace_id is None:
			raise TypeError("messageTrace_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["messageTrace%2Did"] =  messageTrace_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

