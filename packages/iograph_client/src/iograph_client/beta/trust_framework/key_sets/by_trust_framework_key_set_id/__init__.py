# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .upload_secret import UploadSecretRequest
	from .upload_pkcs12 import UploadPkcs12Request
	from .upload_certificate import UploadCertificateRequest
	from .get_active_key import GetActiveKeyRequest
	from .generate_key import GenerateKeyRequest
	from .keys_v2 import Keys_v2Request
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.trust_framework_key_set import TrustFrameworkKeySet


class ByTrustFrameworkKeySetIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets/{trustFrameworkKeySet%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TrustFrameworkKeySet:
		"""
		Get trustFrameworkKeySet
		Retrieve the properties and associations for a Trustframeworkkeyset.
		Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-get?view=graph-rest-beta
		"""
		tags = ['trustFramework.trustFrameworkKeySet']

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
		return await self.request_adapter.send_async(request_info, TrustFrameworkKeySet, error_mapping)

	async def patch(
		self,
		body: TrustFrameworkKeySet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TrustFrameworkKeySet:
		"""
		Update trustFrameworkKeySet
		Update the properties of a trustFrameworkKeyset. This operation will replace the content of an existing keyset. Specifying the ID in the request payload is optional.
		Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-update?view=graph-rest-beta
		"""
		tags = ['trustFramework.trustFrameworkKeySet']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, TrustFrameworkKeySet, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete trustFrameworkKeySet
		Delete a trustFrameworkKeySet.
		Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-delete?view=graph-rest-beta
		"""
		tags = ['trustFramework.trustFrameworkKeySet']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByTrustFrameworkKeySetIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTrustFrameworkKeySetIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTrustFrameworkKeySetIdRequest(self.request_adapter, self.path_parameters)

	def keys_v2(self,
		trustFrameworkKeySet_id: str,
	) -> Keys_v2Request:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .keys_v2 import Keys_v2Request
		return Keys_v2Request(self.request_adapter, path_parameters)

	def generate_key(self,
		trustFrameworkKeySet_id: str,
	) -> GenerateKeyRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .generate_key import GenerateKeyRequest
		return GenerateKeyRequest(self.request_adapter, path_parameters)

	def get_active_key(self,
		trustFrameworkKeySet_id: str,
	) -> GetActiveKeyRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .get_active_key import GetActiveKeyRequest
		return GetActiveKeyRequest(self.request_adapter, path_parameters)

	def upload_certificate(self,
		trustFrameworkKeySet_id: str,
	) -> UploadCertificateRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .upload_certificate import UploadCertificateRequest
		return UploadCertificateRequest(self.request_adapter, path_parameters)

	def upload_pkcs12(self,
		trustFrameworkKeySet_id: str,
	) -> UploadPkcs12Request:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .upload_pkcs12 import UploadPkcs12Request
		return UploadPkcs12Request(self.request_adapter, path_parameters)

	def upload_secret(self,
		trustFrameworkKeySet_id: str,
	) -> UploadSecretRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .upload_secret import UploadSecretRequest
		return UploadSecretRequest(self.request_adapter, path_parameters)

