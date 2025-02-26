# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.add_post_request import AddPostRequest
from iograph_models.models.workbook_table import WorkbookTable
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class AddRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/add"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: AddPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookTable:
		"""
		Invoke action add
		Create a new table. The range source address determines the worksheet under which the table will be added. If the table can't be added (for example, because the address is invalid, or the table would overlap with another table), an error is generated.
		Find more info here: https://learn.microsoft.com/graph/api/tablecollection-add?view=graph-rest-1.0
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookTable, error_mapping)


