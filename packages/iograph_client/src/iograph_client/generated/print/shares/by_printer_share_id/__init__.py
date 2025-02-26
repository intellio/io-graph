# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .printer import PrinterRequest
	from .jobs import JobsRequest
	from .allowed_users import AllowedUsersRequest
	from .allowed_groups import AllowedGroupsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.printer_share import PrinterShare
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrinterShareIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/print/shares/{printerShare%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrinterShare:
		"""
		Get printerShare
		Retrieve the properties and relationships of a printer share.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-get?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, PrinterShare, error_mapping)

	async def patch(
		self,
		body: PrinterShare,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrinterShare:
		"""
		Update printerShare
		Update the properties of a printer share. This method can be used to swap printers. For example, if a physical printer device breaks, an administrator can register a new printer device and update this printerShare to point to the new printer without requiring users to take any action.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-update?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, PrinterShare, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete printerShare
		Delete a printer share (unshare the associated printer). This action can't be undone. If the printer is shared again in the future, any Windows users who had previously installed the printer needs to discover and reinstall it.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-delete?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']
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



	@property
	def allowed_groups(self,
	) -> AllowedGroupsRequest:
		from .allowed_groups import AllowedGroupsRequest
		return AllowedGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def allowed_users(self,
	) -> AllowedUsersRequest:
		from .allowed_users import AllowedUsersRequest
		return AllowedUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def jobs(self,
	) -> JobsRequest:
		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, self.path_parameters)

	@property
	def printer(self,
	) -> PrinterRequest:
		from .printer import PrinterRequest
		return PrinterRequest(self.request_adapter, self.path_parameters)

