# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .mailbox_settings import MailboxSettingsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.user import User
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/subjectRightsRequests/{subjectRightsRequest%2Did}/collaborators/{user%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		Get collaborators from security
		Collection of users who can collaborate on the request.
		"""
		tags = ['security.subjectRightsRequest']

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
		return await self.request_adapter.send_async(request_info, User, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserIdRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_settings(self,
	) -> MailboxSettingsRequest:
		from .mailbox_settings import MailboxSettingsRequest
		return MailboxSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_provisioning_errors(self,
	) -> ServiceProvisioningErrorsRequest:
		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, self.path_parameters)

