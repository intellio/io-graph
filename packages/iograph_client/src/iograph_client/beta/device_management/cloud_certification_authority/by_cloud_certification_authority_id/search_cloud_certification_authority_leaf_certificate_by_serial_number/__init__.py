# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.search_cloud_certification_authority_leaf_certificate_by_serial_number_post_request import Search_cloud_certification_authority_leaf_certificate_by_serial_numberPostRequest


class SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/cloudCertificationAuthority/{cloudCertificationAuthority%2Did}/searchCloudCertificationAuthorityLeafCertificateBySerialNumber", path_parameters)

	async def post(
		self,
		body: Search_cloud_certification_authority_leaf_certificate_by_serial_numberPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudCertificationAuthorityLeafCertificate:
		"""
		Invoke action searchCloudCertificationAuthorityLeafCertificateBySerialNumber
		
		"""
		tags = ['deviceManagement.cloudCertificationAuthority']

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
		return await self.request_adapter.send_async(request_info, CloudCertificationAuthorityLeafCertificate, error_mapping)


	def with_url(self, raw_url: str) -> SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest(self.request_adapter, self.path_parameters)

