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
	from .ref import RefRequest
	from .......request_adapter import HttpxRequestAdapter


class ByUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare-id}/allowedUsers/{user-id}", path_parameters)

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
	def ref(self,
	) -> RefRequest:
		from .ref import RefRequest
		return RefRequest(self.request_adapter, self.path_parameters)

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

