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
	from .upload_new_version import UploadNewVersionRequest
	from .update_language_files import UpdateLanguageFilesRequest
	from .remove_language_files import RemoveLanguageFilesRequest
	from .remove import RemoveRequest
	from .add_language_files import AddLanguageFilesRequest
	from .group_policy_operations import GroupPolicyOperationsRequest
	from .definitions import DefinitionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile


class ByGroupPolicyUploadedDefinitionFileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyUploadedDefinitionFiles/{groupPolicyUploadedDefinitionFile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyUploadedDefinitionFile:
		"""
		Get groupPolicyUploadedDefinitionFiles from deviceManagement
		The available group policy uploaded definition files for this account.
		"""
		tags = ['deviceManagement.groupPolicyUploadedDefinitionFile']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyUploadedDefinitionFile, error_mapping)

	async def patch(
		self,
		body: GroupPolicyUploadedDefinitionFile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyUploadedDefinitionFile:
		"""
		Update the navigation property groupPolicyUploadedDefinitionFiles in deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyUploadedDefinitionFile']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyUploadedDefinitionFile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property groupPolicyUploadedDefinitionFiles for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyUploadedDefinitionFile']
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



	def with_url(self, raw_url: str) -> ByGroupPolicyUploadedDefinitionFileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupPolicyUploadedDefinitionFileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupPolicyUploadedDefinitionFileIdRequest(self.request_adapter, self.path_parameters)

	def definitions(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> DefinitionsRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .definitions import DefinitionsRequest
		return DefinitionsRequest(self.request_adapter, path_parameters)

	def group_policy_operations(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> GroupPolicyOperationsRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .group_policy_operations import GroupPolicyOperationsRequest
		return GroupPolicyOperationsRequest(self.request_adapter, path_parameters)

	def add_language_files(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> AddLanguageFilesRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .add_language_files import AddLanguageFilesRequest
		return AddLanguageFilesRequest(self.request_adapter, path_parameters)

	def remove(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> RemoveRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .remove import RemoveRequest
		return RemoveRequest(self.request_adapter, path_parameters)

	def remove_language_files(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> RemoveLanguageFilesRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .remove_language_files import RemoveLanguageFilesRequest
		return RemoveLanguageFilesRequest(self.request_adapter, path_parameters)

	def update_language_files(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> UpdateLanguageFilesRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .update_language_files import UpdateLanguageFilesRequest
		return UpdateLanguageFilesRequest(self.request_adapter, path_parameters)

	def upload_new_version(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> UploadNewVersionRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .upload_new_version import UploadNewVersionRequest
		return UploadNewVersionRequest(self.request_adapter, path_parameters)

