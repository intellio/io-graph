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
	from .windows_updates_remove_members_by_id import WindowsUpdatesRemoveMembersByIdRequest
	from .windows_updates_remove_members import WindowsUpdatesRemoveMembersRequest
	from .windows_updates_add_members_by_id import WindowsUpdatesAddMembersByIdRequest
	from .windows_updates_add_members import WindowsUpdatesAddMembersRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset


class ByUpdatableAssetIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deploymentAudiences/{deploymentAudience%2Did}/exclusions/{updatableAsset%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesUpdatableAsset:
		"""
		Get exclusions from admin
		Specifies the assets to exclude from the audience.
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatableAsset, error_mapping)

	async def patch(
		self,
		body: WindowsUpdatesUpdatableAsset,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesUpdatableAsset:
		"""
		Update the navigation property exclusions in admin
		
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatableAsset, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property exclusions for admin
		
		"""
		tags = ['admin.adminWindows']
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



	def with_url(self, raw_url: str) -> ByUpdatableAssetIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUpdatableAssetIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUpdatableAssetIdRequest(self.request_adapter, self.path_parameters)

	def windows_updates_add_members(self,
		deploymentAudience_id: str,
		updatableAsset_id: str,
	) -> WindowsUpdatesAddMembersRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")
		if updatableAsset_id is None:
			raise TypeError("updatableAsset_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id
		path_parameters["updatableAsset%2Did"] =  updatableAsset_id

		from .windows_updates_add_members import WindowsUpdatesAddMembersRequest
		return WindowsUpdatesAddMembersRequest(self.request_adapter, path_parameters)

	def windows_updates_add_members_by_id(self,
		deploymentAudience_id: str,
		updatableAsset_id: str,
	) -> WindowsUpdatesAddMembersByIdRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")
		if updatableAsset_id is None:
			raise TypeError("updatableAsset_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id
		path_parameters["updatableAsset%2Did"] =  updatableAsset_id

		from .windows_updates_add_members_by_id import WindowsUpdatesAddMembersByIdRequest
		return WindowsUpdatesAddMembersByIdRequest(self.request_adapter, path_parameters)

	def windows_updates_remove_members(self,
		deploymentAudience_id: str,
		updatableAsset_id: str,
	) -> WindowsUpdatesRemoveMembersRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")
		if updatableAsset_id is None:
			raise TypeError("updatableAsset_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id
		path_parameters["updatableAsset%2Did"] =  updatableAsset_id

		from .windows_updates_remove_members import WindowsUpdatesRemoveMembersRequest
		return WindowsUpdatesRemoveMembersRequest(self.request_adapter, path_parameters)

	def windows_updates_remove_members_by_id(self,
		deploymentAudience_id: str,
		updatableAsset_id: str,
	) -> WindowsUpdatesRemoveMembersByIdRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")
		if updatableAsset_id is None:
			raise TypeError("updatableAsset_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id
		path_parameters["updatableAsset%2Did"] =  updatableAsset_id

		from .windows_updates_remove_members_by_id import WindowsUpdatesRemoveMembersByIdRequest
		return WindowsUpdatesRemoveMembersByIdRequest(self.request_adapter, path_parameters)

