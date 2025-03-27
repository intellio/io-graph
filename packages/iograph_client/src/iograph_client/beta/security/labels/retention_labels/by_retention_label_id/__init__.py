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
	from .retention_event_type import RetentionEventTypeRequest
	from .disposition_review_stages import DispositionReviewStagesRequest
	from .descriptors import DescriptorsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_retention_label import SecurityRetentionLabel
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByRetentionLabelIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/labels/retentionLabels/{retentionLabel%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityRetentionLabel:
		"""
		Get retentionLabels from security
		Represents how customers can manage their data, whether and for how long to retain or delete it.
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityRetentionLabel, error_mapping)

	async def patch(
		self,
		body: SecurityRetentionLabel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityRetentionLabel:
		"""
		Update retentionLabel
		Update the properties of a retentionLabel object. To update a disposition review stage, include the actionAfterRetentionPeriod property in the request body with one of the possible values specified.
		Find more info here: https://learn.microsoft.com/graph/api/security-retentionlabel-update?view=graph-rest-beta
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityRetentionLabel, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete retentionLabel
		Delete a retentionLabel object.
		Find more info here: https://learn.microsoft.com/graph/api/security-retentionlabel-delete?view=graph-rest-beta
		"""
		tags = ['security.labelsRoot']
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



	def with_url(self, raw_url: str) -> ByRetentionLabelIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByRetentionLabelIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByRetentionLabelIdRequest(self.request_adapter, self.path_parameters)

	def descriptors(self,
		retentionLabel_id: str,
	) -> DescriptorsRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .descriptors import DescriptorsRequest
		return DescriptorsRequest(self.request_adapter, path_parameters)

	def disposition_review_stages(self,
		retentionLabel_id: str,
	) -> DispositionReviewStagesRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .disposition_review_stages import DispositionReviewStagesRequest
		return DispositionReviewStagesRequest(self.request_adapter, path_parameters)

	def retention_event_type(self,
		retentionLabel_id: str,
	) -> RetentionEventTypeRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .retention_event_type import RetentionEventTypeRequest
		return RetentionEventTypeRequest(self.request_adapter, path_parameters)

