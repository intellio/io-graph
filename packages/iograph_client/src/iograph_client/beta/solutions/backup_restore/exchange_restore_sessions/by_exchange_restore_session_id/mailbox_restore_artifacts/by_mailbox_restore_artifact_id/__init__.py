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
	from .restore_point import RestorePointRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.mailbox_restore_artifact import MailboxRestoreArtifact


class ByMailboxRestoreArtifactIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeRestoreSessions/{exchangeRestoreSession%2Did}/mailboxRestoreArtifacts/{mailboxRestoreArtifact%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxRestoreArtifact:
		"""
		Get mailboxRestoreArtifacts from solutions
		A collection of restore points and destination details that can be used to restore Exchange mailboxes.
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, MailboxRestoreArtifact, error_mapping)

	async def patch(
		self,
		body: MailboxRestoreArtifact,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MailboxRestoreArtifact:
		"""
		Update the navigation property mailboxRestoreArtifacts in solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, MailboxRestoreArtifact, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property mailboxRestoreArtifacts for solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']
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



	def with_url(self, raw_url: str) -> ByMailboxRestoreArtifactIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMailboxRestoreArtifactIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMailboxRestoreArtifactIdRequest(self.request_adapter, self.path_parameters)

	def restore_point(self,
		exchangeRestoreSession_id: str,
		mailboxRestoreArtifact_id: str,
	) -> RestorePointRequest:
		if exchangeRestoreSession_id is None:
			raise TypeError("exchangeRestoreSession_id cannot be null.")
		if mailboxRestoreArtifact_id is None:
			raise TypeError("mailboxRestoreArtifact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exchangeRestoreSession%2Did"] =  exchangeRestoreSession_id
		path_parameters["mailboxRestoreArtifact%2Did"] =  mailboxRestoreArtifact_id

		from .restore_point import RestorePointRequest
		return RestorePointRequest(self.request_adapter, path_parameters)

