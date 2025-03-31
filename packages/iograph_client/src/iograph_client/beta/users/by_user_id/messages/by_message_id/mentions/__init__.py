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
	from .by_mention_id import ByMentionIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.mention_collection_response import MentionCollectionResponse
from iograph_models.beta.mention import Mention
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MentionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/messages/{message%2Did}/mentions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MentionCollectionResponse:
		"""
		Get mentions from users
		A collection of mentions in the message, ordered by the createdDateTime from the newest to the oldest. By default, a GET /messages does not return this property unless you apply $expand on the property.
		"""
		tags = ['users.message']

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
		return await self.request_adapter.send_async(request_info, MentionCollectionResponse, error_mapping)

	async def post(
		self,
		body: Mention,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Mention:
		"""
		Create new navigation property to mentions for users
		
		"""
		tags = ['users.message']

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
		return await self.request_adapter.send_async(request_info, Mention, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MentionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MentionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MentionsRequest(self.request_adapter, self.path_parameters)

	def by_mention_id(self,
		user_id: str,
		message_id: str,
		mention_id: str,
	) -> ByMentionIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if message_id is None:
			raise TypeError("message_id cannot be null.")
		if mention_id is None:
			raise TypeError("mention_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["message%2Did"] =  message_id
		path_parameters["mention%2Did"] =  mention_id

		from .by_mention_id import ByMentionIdRequest
		return ByMentionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		message_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["message%2Did"] =  message_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

