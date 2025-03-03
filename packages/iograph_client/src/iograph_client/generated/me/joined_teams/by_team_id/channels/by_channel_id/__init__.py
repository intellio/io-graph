# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
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
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.channel import Channel
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByChannelIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/joinedTeams/{team%2Did}/channels/{channel%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Channel:
		"""
		Get channels from me
		The collection of channels and messages associated with the team.
		"""
		tags = ['me.team']

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
		Update the navigation property channels in me
		
		"""
		tags = ['me.team']

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
		Delete navigation property channels for me
		
		"""
		tags = ['me.team']
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

	@property
	def all_members(self,
	) -> AllMembersRequest:
		from .all_members import AllMembersRequest
		return AllMembersRequest(self.request_adapter, self.path_parameters)

	@property
	def files_folder(self,
	) -> FilesFolderRequest:
		from .files_folder import FilesFolderRequest
		return FilesFolderRequest(self.request_adapter, self.path_parameters)

	@property
	def members(self,
	) -> MembersRequest:
		from .members import MembersRequest
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def messages(self,
	) -> MessagesRequest:
		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, self.path_parameters)

	@property
	def archive(self,
	) -> ArchiveRequest:
		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def complete_migration(self,
	) -> CompleteMigrationRequest:
		from .complete_migration import CompleteMigrationRequest
		return CompleteMigrationRequest(self.request_adapter, self.path_parameters)

	@property
	def provision_email(self,
	) -> ProvisionEmailRequest:
		from .provision_email import ProvisionEmailRequest
		return ProvisionEmailRequest(self.request_adapter, self.path_parameters)

	@property
	def remove_email(self,
	) -> RemoveEmailRequest:
		from .remove_email import RemoveEmailRequest
		return RemoveEmailRequest(self.request_adapter, self.path_parameters)

	@property
	def unarchive(self,
	) -> UnarchiveRequest:
		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def shared_with_teams(self,
	) -> SharedWithTeamsRequest:
		from .shared_with_teams import SharedWithTeamsRequest
		return SharedWithTeamsRequest(self.request_adapter, self.path_parameters)

	@property
	def tabs(self,
	) -> TabsRequest:
		from .tabs import TabsRequest
		return TabsRequest(self.request_adapter, self.path_parameters)

