# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.security_retention_label import SecurityRetentionLabel
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByRetentionLabelIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/labels/retentionLabels/{retentionLabel%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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
		Find more info here: https://learn.microsoft.com/graph/api/security-retentionlabel-update?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/security-retentionlabel-delete?view=graph-rest-1.0
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



	@property
	def descriptors(self,
	) -> DescriptorsRequest:
		from .descriptors import DescriptorsRequest
		return DescriptorsRequest(self.request_adapter, self.path_parameters)

	@property
	def disposition_review_stages(self,
	) -> DispositionReviewStagesRequest:
		from .disposition_review_stages import DispositionReviewStagesRequest
		return DispositionReviewStagesRequest(self.request_adapter, self.path_parameters)

	@property
	def retention_event_type(self,
	) -> RetentionEventTypeRequest:
		from .retention_event_type import RetentionEventTypeRequest
		return RetentionEventTypeRequest(self.request_adapter, self.path_parameters)

