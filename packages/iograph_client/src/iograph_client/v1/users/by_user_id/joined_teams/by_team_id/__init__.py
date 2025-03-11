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
	from .template import TemplateRequest
	from .tags import TagsRequest
	from .schedule import ScheduleRequest
	from .primary_channel import PrimaryChannelRequest
	from .photo import PhotoRequest
	from .permission_grants import PermissionGrantsRequest
	from .operations import OperationsRequest
	from .unarchive import UnarchiveRequest
	from .send_activity_notification import SendActivityNotificationRequest
	from .complete_migration import CompleteMigrationRequest
	from .clone import CloneRequest
	from .archive import ArchiveRequest
	from .members import MembersRequest
	from .installed_apps import InstalledAppsRequest
	from .incoming_channels import IncomingChannelsRequest
	from .group import GroupRequest
	from .channels import ChannelsRequest
	from .all_channels import AllChannelsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.team import Team


class ByTeamIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Team:
		"""
		Get joinedTeams from users
		
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
		return await self.request_adapter.send_async(request_info, Team, error_mapping)

	async def patch(
		self,
		body: Team,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Team:
		"""
		Update the navigation property joinedTeams in users
		
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
		return await self.request_adapter.send_async(request_info, Team, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property joinedTeams for users
		
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



	def with_url(self, raw_url: str) -> ByTeamIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTeamIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTeamIdRequest(self.request_adapter, self.path_parameters)

	def all_channels(self,
		user_id: str,
		team_id: str,
	) -> AllChannelsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .all_channels import AllChannelsRequest
		return AllChannelsRequest(self.request_adapter, path_parameters)

	def channels(self,
		user_id: str,
		team_id: str,
	) -> ChannelsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .channels import ChannelsRequest
		return ChannelsRequest(self.request_adapter, path_parameters)

	def group(self,
		user_id: str,
		team_id: str,
	) -> GroupRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def incoming_channels(self,
		user_id: str,
		team_id: str,
	) -> IncomingChannelsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .incoming_channels import IncomingChannelsRequest
		return IncomingChannelsRequest(self.request_adapter, path_parameters)

	def installed_apps(self,
		user_id: str,
		team_id: str,
	) -> InstalledAppsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, path_parameters)

	def members(self,
		user_id: str,
		team_id: str,
	) -> MembersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def archive(self,
		user_id: str,
		team_id: str,
	) -> ArchiveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, path_parameters)

	def clone(self,
		user_id: str,
		team_id: str,
	) -> CloneRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .clone import CloneRequest
		return CloneRequest(self.request_adapter, path_parameters)

	def complete_migration(self,
		user_id: str,
		team_id: str,
	) -> CompleteMigrationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, path_parameters)

	def send_activity_notification(self,
		user_id: str,
		team_id: str,
	) -> SendActivityNotificationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, path_parameters)

	def unarchive(self,
		user_id: str,
		team_id: str,
	) -> UnarchiveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, path_parameters)

	def operations(self,
		user_id: str,
		team_id: str,
	) -> OperationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		user_id: str,
		team_id: str,
	) -> PermissionGrantsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def photo(self,
		user_id: str,
		team_id: str,
	) -> PhotoRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

	def primary_channel(self,
		user_id: str,
		team_id: str,
	) -> PrimaryChannelRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .primary_channel import PrimaryChannelRequest
		return PrimaryChannelRequest(self.request_adapter, path_parameters)

	def schedule(self,
		user_id: str,
		team_id: str,
	) -> ScheduleRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .schedule import ScheduleRequest
		return ScheduleRequest(self.request_adapter, path_parameters)

	def tags(self,
		user_id: str,
		team_id: str,
	) -> TagsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, path_parameters)

	def template(self,
		user_id: str,
		team_id: str,
	) -> TemplateRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .template import TemplateRequest
		return TemplateRequest(self.request_adapter, path_parameters)

