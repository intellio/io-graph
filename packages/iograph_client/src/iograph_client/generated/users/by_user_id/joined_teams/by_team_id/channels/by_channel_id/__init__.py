# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tabs import TabsRequest
	from .shared_with_teams import SharedWithTeamsRequest
	from .unarchive import UnarchiveRequest
	from .remove_email import RemoveEmailRequest
	from .provision_email import ProvisionEmailRequest
	from .complete_migration import CompleteMigrationRequest
	from .archive import ArchiveRequest
	from .messages import MessagesRequest
	from .members import MembersRequest
	from .files_folder import FilesFolderRequest
	from .all_members import AllMembersRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.channel import Channel


class ByChannelIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/channels/{channel%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Channel:
		"""
		Get channels from users
		The collection of channels and messages associated with the team.
		"""
		tags = ['users.team']

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
		return await self.request_adapter.send_async(request_info, Channel, error_mapping)

	async def patch(
		self,
		body: Channel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Channel:
		"""
		Update the navigation property channels in users
		
		"""
		tags = ['users.team']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Channel, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property channels for users
		
		"""
		tags = ['users.team']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByChannelIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByChannelIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByChannelIdRequest(self.request_adapter, self.path_parameters)

	def all_members(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> AllMembersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .all_members import AllMembersRequest
		return AllMembersRequest(self.request_adapter, path_parameters)

	def files_folder(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> FilesFolderRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .files_folder import FilesFolderRequest
		return FilesFolderRequest(self.request_adapter, path_parameters)

	def members(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> MembersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def messages(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> MessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def archive(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> ArchiveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, path_parameters)

	def complete_migration(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> CompleteMigrationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, path_parameters)

	def provision_email(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> ProvisionEmailRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .provision_email import ProvisionEmailRequest
		return ProvisionEmailRequest(self.request_adapter, path_parameters)

	def remove_email(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> RemoveEmailRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .remove_email import RemoveEmailRequest
		return RemoveEmailRequest(self.request_adapter, path_parameters)

	def unarchive(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> UnarchiveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, path_parameters)

	def shared_with_teams(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> SharedWithTeamsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .shared_with_teams import SharedWithTeamsRequest
		return SharedWithTeamsRequest(self.request_adapter, path_parameters)

	def tabs(self,
		user_id: str,
		team_id: str,
		channel_id: str,
	) -> TabsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .tabs import TabsRequest
		return TabsRequest(self.request_adapter, path_parameters)

