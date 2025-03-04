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
	from .count import CountRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.security_alert_comment import SecurityAlertComment
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CommentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/incidents/{incident%2Did}/alerts/{alert%2Did}/comments", path_parameters)

	async def post(
		self,
		body: list[SecurityAlertComment],
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> list[SecurityAlertComment]:
		"""
		Sets a new value for the collection of alertComment.
		
		"""
		tags = ['security.incident']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

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
		return await self.request_adapter.send_collection_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> CommentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CommentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CommentsRequest(self.request_adapter, self.path_parameters)

	def count(self,
		incident_id: str,
		alert_id: str,
	) -> CountRequest:
		if incident_id is None:
			raise TypeError("incident_id cannot be null.")
		if alert_id is None:
			raise TypeError("alert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["incident%2Did"] =  incident_id
		path_parameters["alert%2Did"] =  alert_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

