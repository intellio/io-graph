# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_cloud_certification_authority_leaf_certificate_id import ByCloudCertificationAuthorityLeafCertificateIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cloud_certification_authority_leaf_certificate_collection_response import CloudCertificationAuthorityLeafCertificateCollectionResponse


class CloudCertificationAuthorityLeafCertificateRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/cloudCertificationAuthority/{cloudCertificationAuthority%2Did}/cloudCertificationAuthorityLeafCertificate", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudCertificationAuthorityLeafCertificateCollectionResponse:
		"""
		Get cloudCertificationAuthorityLeafCertificate from deviceManagement
		Required OData property to expose leaf certificate API.
		"""
		tags = ['deviceManagement.cloudCertificationAuthority']

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
		return await self.request_adapter.send_async(request_info, CloudCertificationAuthorityLeafCertificateCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> CloudCertificationAuthorityLeafCertificateRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CloudCertificationAuthorityLeafCertificateRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CloudCertificationAuthorityLeafCertificateRequest(self.request_adapter, self.path_parameters)

	def by_cloud_certification_authority_leaf_certificate_id(self,
		cloudCertificationAuthority_id: str,
		cloudCertificationAuthorityLeafCertificate_id: str,
	) -> ByCloudCertificationAuthorityLeafCertificateIdRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")
		if cloudCertificationAuthorityLeafCertificate_id is None:
			raise TypeError("cloudCertificationAuthorityLeafCertificate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id
		path_parameters["cloudCertificationAuthorityLeafCertificate%2Did"] =  cloudCertificationAuthorityLeafCertificate_id

		from .by_cloud_certification_authority_leaf_certificate_id import ByCloudCertificationAuthorityLeafCertificateIdRequest
		return ByCloudCertificationAuthorityLeafCertificateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		cloudCertificationAuthority_id: str,
	) -> CountRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

