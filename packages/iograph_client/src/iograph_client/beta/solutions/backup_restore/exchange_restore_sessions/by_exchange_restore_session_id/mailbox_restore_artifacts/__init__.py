# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_mailbox_restore_artifact_id import ByMailboxRestoreArtifactIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.mailbox_restore_artifact_collection_response import MailboxRestoreArtifactCollectionResponse
from iograph_models.beta.mailbox_restore_artifact import MailboxRestoreArtifact


class MailboxRestoreArtifactsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeRestoreSessions/{exchangeRestoreSession%2Did}/mailboxRestoreArtifacts", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxRestoreArtifactCollectionResponse:
		"""
		List mailboxRestoreArtifacts
		Get a list of the mailboxRestoreArtifact objects that are associated with an exchangeRestoreSession in a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/exchangerestoresession-list-mailboxrestoreartifacts?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, MailboxRestoreArtifactCollectionResponse, error_mapping)

	async def post(
		self,
		body: MailboxRestoreArtifact,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MailboxRestoreArtifact:
		"""
		Create new navigation property to mailboxRestoreArtifacts for solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, MailboxRestoreArtifact, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MailboxRestoreArtifactsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MailboxRestoreArtifactsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MailboxRestoreArtifactsRequest(self.request_adapter, self.path_parameters)

	def by_mailbox_restore_artifact_id(self,
		exchangeRestoreSession_id: str,
		mailboxRestoreArtifact_id: str,
	) -> ByMailboxRestoreArtifactIdRequest:
		if exchangeRestoreSession_id is None:
			raise TypeError("exchangeRestoreSession_id cannot be null.")
		if mailboxRestoreArtifact_id is None:
			raise TypeError("mailboxRestoreArtifact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exchangeRestoreSession%2Did"] =  exchangeRestoreSession_id
		path_parameters["mailboxRestoreArtifact%2Did"] =  mailboxRestoreArtifact_id

		from .by_mailbox_restore_artifact_id import ByMailboxRestoreArtifactIdRequest
		return ByMailboxRestoreArtifactIdRequest(self.request_adapter, path_parameters)

	def count(self,
		exchangeRestoreSession_id: str,
	) -> CountRequest:
		if exchangeRestoreSession_id is None:
			raise TypeError("exchangeRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exchangeRestoreSession%2Did"] =  exchangeRestoreSession_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

