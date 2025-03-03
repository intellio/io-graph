# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
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
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.team import Team
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class TeamRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/team", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Team:
		"""
		Get team from groups
		The team associated with this group.
		"""
		tags = ['groups.team']

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

	async def put(
		self,
		body: Team,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Team:
		"""
		Create team from group
		Create a new team under a group. In order to create a team, the group must have a least one owner. If the creation of the team call is delayed, you can retry the call up to three times before you have to wait for 15 minutes due to a propagation delay. If the group was created less than 15 minutes ago, the call might fail with a 404 error code due to replication delays. If the group was created less than 15 minutes ago, it's possible for a call to create a team to fail with a 404 error code, due to ongoing replication delays.
The recommended pattern is to retry the Create team call three times, with a 10 second delay between calls.
		Find more info here: https://learn.microsoft.com/graph/api/team-put-teams?view=graph-rest-1.0
		"""
		tags = ['groups.team']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
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
		Delete navigation property team for groups
		
		"""
		tags = ['groups.team']
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



	def with_url(self, raw_url: str) -> TeamRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TeamRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TeamRequest(self.request_adapter, self.path_parameters)

	@property
	def all_channels(self,
	) -> AllChannelsRequest:
		from .all_channels import AllChannelsRequest
		return AllChannelsRequest(self.request_adapter, self.path_parameters)

	@property
	def channels(self,
	) -> ChannelsRequest:
		from .channels import ChannelsRequest
		return ChannelsRequest(self.request_adapter, self.path_parameters)

	@property
	def group(self,
	) -> GroupRequest:
		from .group import GroupRequest
		return GroupRequest(self.request_adapter, self.path_parameters)

	@property
	def incoming_channels(self,
	) -> IncomingChannelsRequest:
		from .incoming_channels import IncomingChannelsRequest
		return IncomingChannelsRequest(self.request_adapter, self.path_parameters)

	@property
	def installed_apps(self,
	) -> InstalledAppsRequest:
		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def members(self,
	) -> MembersRequest:
		from .members import MembersRequest
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def archive(self,
	) -> ArchiveRequest:
		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def clone(self,
	) -> CloneRequest:
		from .clone import CloneRequest
		return CloneRequest(self.request_adapter, self.path_parameters)

	@property
	def complete_migration(self,
	) -> CompleteMigrationRequest:
		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, self.path_parameters)

	@property
	def send_activity_notification(self,
	) -> SendActivityNotificationRequest:
		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, self.path_parameters)

	@property
	def unarchive(self,
	) -> UnarchiveRequest:
		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grants(self,
	) -> PermissionGrantsRequest:
		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def photo(self,
	) -> PhotoRequest:
		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, self.path_parameters)

	@property
	def primary_channel(self,
	) -> PrimaryChannelRequest:
		from .primary_channel import PrimaryChannelRequest
		return PrimaryChannelRequest(self.request_adapter, self.path_parameters)

	@property
	def schedule(self,
	) -> ScheduleRequest:
		from .schedule import ScheduleRequest
		return ScheduleRequest(self.request_adapter, self.path_parameters)

	@property
	def tags(self,
	) -> TagsRequest:
		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, self.path_parameters)

	@property
	def template(self,
	) -> TemplateRequest:
		from .template import TemplateRequest
		return TemplateRequest(self.request_adapter, self.path_parameters)

