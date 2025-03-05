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
	from .count import CountRequest
	from .by_message_rule_id import ByMessageRuleIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.message_rule import MessageRule
from iograph_models.models.message_rule_collection_response import MessageRuleCollectionResponse


class MessageRulesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}/childFolders/{mailFolder%2Did1}/messageRules", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MessageRuleCollectionResponse:
		"""
		Get messageRules from users
		The collection of rules that apply to the user's Inbox folder.
		"""
		tags = ['users.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MessageRuleCollectionResponse, error_mapping)

	async def post(
		self,
		body: MessageRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MessageRule:
		"""
		Create new navigation property to messageRules for users
		
		"""
		tags = ['users.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MessageRule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MessageRulesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MessageRulesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MessageRulesRequest(self.request_adapter, self.path_parameters)

	def by_message_rule_id(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
		messageRule_id: str,
	) -> ByMessageRuleIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")
		if messageRule_id is None:
			raise TypeError("messageRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1
		path_parameters["messageRule%2Did"] =  messageRule_id

		from .by_message_rule_id import ByMessageRuleIdRequest
		return ByMessageRuleIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

