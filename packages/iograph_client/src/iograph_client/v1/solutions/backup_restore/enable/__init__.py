# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.enable_post_request import EnablePostRequest
from iograph_models.v1.service_status import ServiceStatus


class EnableRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/enable", path_parameters)

	async def post(
		self,
		body: EnablePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServiceStatus:
		"""
		Invoke action enable
		Enable the Microsoft 365 Backup Storage service for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-enable?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ServiceStatus, error_mapping)


	def with_url(self, raw_url: str) -> EnableRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EnableRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EnableRequest(self.request_adapter, self.path_parameters)

