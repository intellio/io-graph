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
	from .template_definition import TemplateDefinitionRequest
	from .template import TemplateRequest
	from .tags import TagsRequest
	from .schedule import ScheduleRequest
	from .primary_channel import PrimaryChannelRequest
	from .photo import PhotoRequest
	from .permission_grants import PermissionGrantsRequest
	from .owners_with_userprincipalname import OwnersWithUserPrincipalNameRequest
	from .owners import OwnersRequest
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
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.team import Team
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class TeamDefinitionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/teamTemplates/{teamTemplate%2Did}/definitions/{teamTemplateDefinition%2Did}/teamDefinition", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Team:
		"""
		Get teamDefinition
		Get the properties of the team associated with a teamTemplateDefinition object.
		Find more info here: https://learn.microsoft.com/graph/api/teamtemplatedefinition-get-teamdefinition?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Team, error_mapping)

	async def patch(
		self,
		body: Team,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Team:
		"""
		Update the navigation property teamDefinition in teamwork
		
		"""
		tags = ['teamwork.teamTemplate']

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
		Delete navigation property teamDefinition for teamwork
		
		"""
		tags = ['teamwork.teamTemplate']
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



	def with_url(self, raw_url: str) -> TeamDefinitionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TeamDefinitionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TeamDefinitionRequest(self.request_adapter, self.path_parameters)

	def all_channels(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> AllChannelsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .all_channels import AllChannelsRequest
		return AllChannelsRequest(self.request_adapter, path_parameters)

	def channels(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> ChannelsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .channels import ChannelsRequest
		return ChannelsRequest(self.request_adapter, path_parameters)

	def group(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> GroupRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def incoming_channels(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> IncomingChannelsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .incoming_channels import IncomingChannelsRequest
		return IncomingChannelsRequest(self.request_adapter, path_parameters)

	def installed_apps(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> InstalledAppsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, path_parameters)

	def members(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> MembersRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def archive(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> ArchiveRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, path_parameters)

	def clone(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> CloneRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .clone import CloneRequest
		return CloneRequest(self.request_adapter, path_parameters)

	def complete_migration(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> CompleteMigrationRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, path_parameters)

	def send_activity_notification(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> SendActivityNotificationRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, path_parameters)

	def unarchive(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> UnarchiveRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, path_parameters)

	def operations(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> OperationsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def owners(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> OwnersRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

	def owners_with_userprincipalname(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		userPrincipalName: str,
	) -> OwnersWithUserPrincipalNameRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if userPrincipalName is None:
			raise TypeError("userPrincipalName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["userPrincipalName"] =  userPrincipalName

		from .owners_with_userprincipalname import OwnersWithUserPrincipalNameRequest
		return OwnersWithUserPrincipalNameRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> PermissionGrantsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def photo(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> PhotoRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

	def primary_channel(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> PrimaryChannelRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .primary_channel import PrimaryChannelRequest
		return PrimaryChannelRequest(self.request_adapter, path_parameters)

	def schedule(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> ScheduleRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .schedule import ScheduleRequest
		return ScheduleRequest(self.request_adapter, path_parameters)

	def tags(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> TagsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, path_parameters)

	def template(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> TemplateRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .template import TemplateRequest
		return TemplateRequest(self.request_adapter, path_parameters)

	def template_definition(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> TemplateDefinitionRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .template_definition import TemplateDefinitionRequest
		return TemplateDefinitionRequest(self.request_adapter, path_parameters)

