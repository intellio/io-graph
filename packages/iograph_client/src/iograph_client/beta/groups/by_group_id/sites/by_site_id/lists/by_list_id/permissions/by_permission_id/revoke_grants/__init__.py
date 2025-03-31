# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.permission import Permission
from iograph_models.beta.revoke_grants_post_request import Revoke_grantsPostRequest


class RevokeGrantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/lists/{list%2Did}/permissions/{permission%2Did}/revokeGrants", path_parameters)

	async def post(
		self,
		body: Revoke_grantsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Permission:
		"""
		Invoke action revokeGrants
		Revoke access to a listItem or driveItem granted via a sharing link by removing the specified recipient from the link.
		Find more info here: https://learn.microsoft.com/graph/api/permission-revokegrants?view=graph-rest-beta
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, Permission, error_mapping)


	def with_url(self, raw_url: str) -> RevokeGrantsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RevokeGrantsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RevokeGrantsRequest(self.request_adapter, self.path_parameters)

