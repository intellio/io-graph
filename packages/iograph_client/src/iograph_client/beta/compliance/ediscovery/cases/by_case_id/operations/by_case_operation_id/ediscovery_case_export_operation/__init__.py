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
	from .review_set import ReviewSetRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_case_export_operation import EdiscoveryCaseExportOperation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class EdiscoveryCaseExportOperationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/operations/{caseOperation%2Did}/microsoft.graph.ediscovery.caseExportOperation", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryCaseExportOperation:
		"""
		Get the item of type microsoft.graph.ediscovery.caseOperation as microsoft.graph.ediscovery.caseExportOperation
		
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryCaseExportOperation, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> EdiscoveryCaseExportOperationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EdiscoveryCaseExportOperationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EdiscoveryCaseExportOperationRequest(self.request_adapter, self.path_parameters)

	def review_set(self,
		case_id: str,
		caseOperation_id: str,
	) -> ReviewSetRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if caseOperation_id is None:
			raise TypeError("caseOperation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["caseOperation%2Did"] =  caseOperation_id

		from .review_set import ReviewSetRequest
		return ReviewSetRequest(self.request_adapter, path_parameters)

