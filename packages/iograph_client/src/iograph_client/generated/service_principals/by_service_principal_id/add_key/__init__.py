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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.key_credential import KeyCredential
from iograph_models.models.add_key_post_request import Add_keyPostRequest


class AddKeyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/addKey", path_parameters)

	async def post(
		self,
		body: Add_keyPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> KeyCredential:
		"""
		Invoke action addKey
		Adds a key credential to a servicePrincipal. This method along with removeKey can be used by a servicePrincipal to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.  ServicePrincipals that don’t have any existing valid certificates (i.e.: no certificates have been added yet, or all certificates have expired), won’t be able to use this service action. Update servicePrincipal can be used to perform an update instead.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-addkey?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal.Actions']

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
		return await self.request_adapter.send_async(request_info, KeyCredential, error_mapping)


	def with_url(self, raw_url: str) -> AddKeyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AddKeyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AddKeyRequest(self.request_adapter, self.path_parameters)

