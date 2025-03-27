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
	from .security_extract_content_label import SecurityExtractContentLabelRequest
	from .security_evaluate_removal import SecurityEvaluateRemovalRequest
	from .security_evaluate_classification_results import SecurityEvaluateClassificationResultsRequest
	from .security_evaluate_application import SecurityEvaluateApplicationRequest
	from .count import CountRequest
	from .by_sensitivity_label_id import BySensitivityLabelIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_sensitivity_label import SecuritySensitivityLabel
from iograph_models.beta.security_sensitivity_label_collection_response import SecuritySensitivityLabelCollectionResponse


class SensitivityLabelsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/informationProtection/sensitivityLabels", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecuritySensitivityLabelCollectionResponse:
		"""
		Get sensitivityLabels from security
		Read the Microsoft Purview Information Protection labels for the user or organization.
		"""
		tags = ['security.informationProtection']

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
		return await self.request_adapter.send_async(request_info, SecuritySensitivityLabelCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecuritySensitivityLabel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecuritySensitivityLabel:
		"""
		Create new navigation property to sensitivityLabels for security
		
		"""
		tags = ['security.informationProtection']

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
		return await self.request_adapter.send_async(request_info, SecuritySensitivityLabel, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SensitivityLabelsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SensitivityLabelsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SensitivityLabelsRequest(self.request_adapter, self.path_parameters)

	def by_sensitivity_label_id(self,
		sensitivityLabel_id: str,
	) -> BySensitivityLabelIdRequest:
		if sensitivityLabel_id is None:
			raise TypeError("sensitivityLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sensitivityLabel%2Did"] =  sensitivityLabel_id

		from .by_sensitivity_label_id import BySensitivityLabelIdRequest
		return BySensitivityLabelIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def security_evaluate_application(self,
	) -> SecurityEvaluateApplicationRequest:
		from .security_evaluate_application import SecurityEvaluateApplicationRequest
		return SecurityEvaluateApplicationRequest(self.request_adapter, self.path_parameters)

	@property
	def security_evaluate_classification_results(self,
	) -> SecurityEvaluateClassificationResultsRequest:
		from .security_evaluate_classification_results import SecurityEvaluateClassificationResultsRequest
		return SecurityEvaluateClassificationResultsRequest(self.request_adapter, self.path_parameters)

	@property
	def security_evaluate_removal(self,
	) -> SecurityEvaluateRemovalRequest:
		from .security_evaluate_removal import SecurityEvaluateRemovalRequest
		return SecurityEvaluateRemovalRequest(self.request_adapter, self.path_parameters)

	@property
	def security_extract_content_label(self,
	) -> SecurityExtractContentLabelRequest:
		from .security_extract_content_label import SecurityExtractContentLabelRequest
		return SecurityExtractContentLabelRequest(self.request_adapter, self.path_parameters)

