# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.assign_license_post_request import Assign_licensePostRequest
from iograph_models.v1.assign_license_response import AssignLicenseResponse


class AssignLicenseRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/assignLicense", path_parameters)

	async def post(
		self,
		body: Assign_licensePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AssignLicenseResponse:
		"""
		Invoke action assignLicense
		Add or remove licenses for the user to enable or disable their use of Microsoft cloud offerings that the company has licenses to. For example, an organization can have a Microsoft 365 Enterprise E3 subscription with 100 licenses, and this request assigns one of those licenses to a specific user. You can also enable and disable specific plans associated with a subscription. Direct user licensing method is an alternative to group-based licensing.
		Find more info here: https://learn.microsoft.com/graph/api/user-assignlicense?view=graph-rest-1.0
		"""
		tags = ['me.user.Actions']

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
		return await self.request_adapter.send_async(request_info, AssignLicenseResponse, error_mapping)


	def with_url(self, raw_url: str) -> AssignLicenseRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignLicenseRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignLicenseRequest(self.request_adapter, self.path_parameters)

