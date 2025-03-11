# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.workbook_table_row import WorkbookTableRow


class TableRowOperationResultWithKeyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tableRowOperationResult(key='{key}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookTableRow:
		"""
		Invoke function tableRowOperationResult
		This function is the last in a series of steps to create a workbookTableRow resource asynchronously. A best practice to create multiple table rows is to batch them in one create tableRow operation and carry out the operation asynchronously. An asynchronous request to create table rows involves the following steps:
1. Issue an async Create tableRow request and get the query URL returned in the Location response header.
2. Use the query URL returned from step 1 to issue the Get workbookOperation request and get the operation ID for step 3. 
    Alternatively, for convenience, after you get a succeeded operationStatus result, you can get the query URL from the resourceLocation property of the workbookOperation returned in the response, and apply the query URL to step 3. 
3. Use the query URL returned from step 2 as the GET request URL for this function tableRowOperationResult. A successful function call returns the new table rows in a workbookTableRow resource. This function does not do anything if called independently.
		Find more info here: https://learn.microsoft.com/graph/api/workbook-tablerowoperationresult?view=graph-rest-1.0
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookTableRow, error_mapping)


	def with_url(self, raw_url: str) -> TableRowOperationResultWithKeyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TableRowOperationResultWithKeyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TableRowOperationResultWithKeyRequest(self.request_adapter, self.path_parameters)

