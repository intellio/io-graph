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
	from .tabs import TabsRequest
	from .shared_with_teams import SharedWithTeamsRequest
	from .planner import PlannerRequest
	from .unarchive import UnarchiveRequest
	from .remove_email import RemoveEmailRequest
	from .provision_email import ProvisionEmailRequest
	from .complete_migration import CompleteMigrationRequest
	from .archive import ArchiveRequest
	from .messages import MessagesRequest
	from .members import MembersRequest
	from .files_folder import FilesFolderRequest
	from .all_members import AllMembersRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.channel import Channel
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PrimaryChannelRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/teamTemplates/{teamTemplate%2Did}/definitions/{teamTemplateDefinition%2Did}/teamDefinition/primaryChannel", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Channel:
		"""
		Get primaryChannel from teamwork
		The general channel for the team.
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
		return await self.request_adapter.send_async(request_info, Channel, error_mapping)

	async def patch(
		self,
		body: Channel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Channel:
		"""
		Update the navigation property primaryChannel in teamwork
		
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
		return await self.request_adapter.send_async(request_info, Channel, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property primaryChannel for teamwork
		
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



	def with_url(self, raw_url: str) -> PrimaryChannelRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PrimaryChannelRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PrimaryChannelRequest(self.request_adapter, self.path_parameters)

	def all_members(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> AllMembersRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .all_members import AllMembersRequest
		return AllMembersRequest(self.request_adapter, path_parameters)

	def files_folder(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> FilesFolderRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .files_folder import FilesFolderRequest
		return FilesFolderRequest(self.request_adapter, path_parameters)

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

	def messages(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> MessagesRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

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

	def provision_email(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> ProvisionEmailRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .provision_email import ProvisionEmailRequest
		return ProvisionEmailRequest(self.request_adapter, path_parameters)

	def remove_email(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> RemoveEmailRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .remove_email import RemoveEmailRequest
		return RemoveEmailRequest(self.request_adapter, path_parameters)

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

	def planner(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> PlannerRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, path_parameters)

	def shared_with_teams(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> SharedWithTeamsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .shared_with_teams import SharedWithTeamsRequest
		return SharedWithTeamsRequest(self.request_adapter, path_parameters)

	def tabs(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
	) -> TabsRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .tabs import TabsRequest
		return TabsRequest(self.request_adapter, path_parameters)

