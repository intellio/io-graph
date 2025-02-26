# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.force_delete_post_request import Force_deletePostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ForceDeleteRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/domains/{domain%2Did}/forceDelete"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Force_deletePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action forceDelete
		Delete a domain using an asynchronous long-running operation. Before performing this operation, you must update or remove any references to Exchange as the provisioning service. The following actions are performed as part of this operation: After the domain deletion completes, API operations for the deleted domain return an HTTP 404 status code. To verify deletion of a domain, you can perform a get domain operation.
		Find more info here: https://learn.microsoft.com/graph/api/domain-forcedelete?view=graph-rest-1.0
		"""
		tags = ['domains.domain.Actions']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


