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
	from .export_items import ExportItemsRequest
	from .create_import_session import CreateImportSessionRequest
	from .folders import FoldersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.mailbox import Mailbox
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMailboxIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/exchange/mailboxes/{mailbox%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Mailbox:
		"""
		Get mailboxes from admin
		Represents a user's mailboxes.
		"""
		tags = ['admin.exchangeAdmin']

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
		return await self.request_adapter.send_async(request_info, Mailbox, error_mapping)

	async def patch(
		self,
		body: Mailbox,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Mailbox:
		"""
		Update the navigation property mailboxes in admin
		
		"""
		tags = ['admin.exchangeAdmin']

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
		return await self.request_adapter.send_async(request_info, Mailbox, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property mailboxes for admin
		
		"""
		tags = ['admin.exchangeAdmin']
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



	def with_url(self, raw_url: str) -> ByMailboxIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMailboxIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMailboxIdRequest(self.request_adapter, self.path_parameters)

	def folders(self,
		mailbox_id: str,
	) -> FoldersRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id

		from .folders import FoldersRequest
		return FoldersRequest(self.request_adapter, path_parameters)

	def create_import_session(self,
		mailbox_id: str,
	) -> CreateImportSessionRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id

		from .create_import_session import CreateImportSessionRequest
		return CreateImportSessionRequest(self.request_adapter, path_parameters)

	def export_items(self,
		mailbox_id: str,
	) -> ExportItemsRequest:
		if mailbox_id is None:
			raise TypeError("mailbox_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailbox%2Did"] =  mailbox_id

		from .export_items import ExportItemsRequest
		return ExportItemsRequest(self.request_adapter, path_parameters)

