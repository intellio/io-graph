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
from iograph_models.v1.self_signed_certificate import SelfSignedCertificate
from iograph_models.v1.add_token_signing_certificate_post_request import Add_token_signing_certificatePostRequest


class AddTokenSigningCertificateRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/addTokenSigningCertificate", path_parameters)

	async def post(
		self,
		body: Add_token_signing_certificatePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SelfSignedCertificate:
		"""
		Invoke action addTokenSigningCertificate
		Create a self-signed signing certificate and return a selfSignedCertificate object, which is the public part of the generated certificate.  The self-signed signing certificate is composed of the following objects, which are added to the servicePrincipal: 
+ The keyCredentials object with the following objects:
    + A private key object with usage set to Sign.
    + A public key object with usage set to Verify.
+ The passwordCredentials object.  All the objects have the same value of customKeyIdentifier. The passwordCredential is used to open the PFX file (private key). It and the associated private key object have the same value of keyId. When set during creation through the displayName property, the subject of the certificate cannot be updated. The startDateTime is set to the same time the certificate is created using the action. The endDateTime can be up to three years after the certificate is created.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-addtokensigningcertificate?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SelfSignedCertificate, error_mapping)


	def with_url(self, raw_url: str) -> AddTokenSigningCertificateRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AddTokenSigningCertificateRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AddTokenSigningCertificateRequest(self.request_adapter, self.path_parameters)

