# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
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
from iograph_models.v1.team import Team
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


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

	def all_channels(self,
		group_id: str,
	) -> AllChannelsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .all_channels import AllChannelsRequest
		return AllChannelsRequest(self.request_adapter, path_parameters)

	def channels(self,
		group_id: str,
	) -> ChannelsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .channels import ChannelsRequest
		return ChannelsRequest(self.request_adapter, path_parameters)

	def group(self,
		group_id: str,
	) -> GroupRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def incoming_channels(self,
		group_id: str,
	) -> IncomingChannelsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .incoming_channels import IncomingChannelsRequest
		return IncomingChannelsRequest(self.request_adapter, path_parameters)

	def installed_apps(self,
		group_id: str,
	) -> InstalledAppsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, path_parameters)

	def members(self,
		group_id: str,
	) -> MembersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def archive(self,
		group_id: str,
	) -> ArchiveRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, path_parameters)

	def clone(self,
		group_id: str,
	) -> CloneRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .clone import CloneRequest
		return CloneRequest(self.request_adapter, path_parameters)

	def complete_migration(self,
		group_id: str,
	) -> CompleteMigrationRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, path_parameters)

	def send_activity_notification(self,
		group_id: str,
	) -> SendActivityNotificationRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, path_parameters)

	def unarchive(self,
		group_id: str,
	) -> UnarchiveRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, path_parameters)

	def operations(self,
		group_id: str,
	) -> OperationsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		group_id: str,
	) -> PermissionGrantsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def photo(self,
		group_id: str,
	) -> PhotoRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

	def primary_channel(self,
		group_id: str,
	) -> PrimaryChannelRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .primary_channel import PrimaryChannelRequest
		return PrimaryChannelRequest(self.request_adapter, path_parameters)

	def schedule(self,
		group_id: str,
	) -> ScheduleRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .schedule import ScheduleRequest
		return ScheduleRequest(self.request_adapter, path_parameters)

	def tags(self,
		group_id: str,
	) -> TagsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, path_parameters)

	def template(self,
		group_id: str,
	) -> TemplateRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .template import TemplateRequest
		return TemplateRequest(self.request_adapter, path_parameters)

