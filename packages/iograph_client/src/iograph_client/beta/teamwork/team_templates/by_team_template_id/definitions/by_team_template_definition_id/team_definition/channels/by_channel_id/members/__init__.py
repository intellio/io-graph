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
	from .remove import RemoveRequest
	from .add import AddRequest
	from .count import CountRequest
	from .by_conversation_member_id import ByConversationMemberIdRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.conversation_member import ConversationMember
from iograph_models.beta.conversation_member_collection_response import ConversationMemberCollectionResponse


class MembersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/teamTemplates/{teamTemplate%2Did}/definitions/{teamTemplateDefinition%2Did}/teamDefinition/channels/{channel%2Did}/members", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ConversationMemberCollectionResponse:
		"""
		Get members from teamwork
		A collection of membership records associated with the channel.
		"""
		tags = ['teamwork.teamTemplate']

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
		return await self.request_adapter.send_async(request_info, ConversationMemberCollectionResponse, error_mapping)

	async def post(
		self,
		body: ConversationMember,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConversationMember:
		"""
		Create new navigation property to members for teamwork
		
		"""
		tags = ['teamwork.teamTemplate']

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
		return await self.request_adapter.send_async(request_info, ConversationMember, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MembersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MembersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MembersRequest(self.request_adapter, self.path_parameters)

	def by_conversation_member_id(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
		conversationMember_id: str,
	) -> ByConversationMemberIdRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if conversationMember_id is None:
			raise TypeError("conversationMember_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["conversationMember%2Did"] =  conversationMember_id

		from .by_conversation_member_id import ByConversationMemberIdRequest
		return ByConversationMemberIdRequest(self.request_adapter, path_parameters)

	def count(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
	) -> CountRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def add(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
	) -> AddRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id

		from .add import AddRequest
		return AddRequest(self.request_adapter, path_parameters)

	def remove(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
	) -> RemoveRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id

		from .remove import RemoveRequest
		return RemoveRequest(self.request_adapter, path_parameters)

