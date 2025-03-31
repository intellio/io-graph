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
	from .extract_label import ExtractLabelRequest
	from .evaluate_removal import EvaluateRemovalRequest
	from .evaluate_classification_results import EvaluateClassificationResultsRequest
	from .evaluate_application import EvaluateApplicationRequest
	from .count import CountRequest
	from .by_information_protection_label_id import ByInformationProtectionLabelIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.information_protection_label import InformationProtectionLabel
from iograph_models.beta.information_protection_label_collection_response import InformationProtectionLabelCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class LabelsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/informationProtection/policy/labels", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InformationProtectionLabelCollectionResponse:
		"""
		informationProtectionLabel: listLabels (deprecated)
		Get a collection of information protection labels available to the user or to the organization.
		Find more info here: https://learn.microsoft.com/graph/api/informationprotectionpolicy-list-labels?view=graph-rest-beta
		"""
		tags = ['me.informationProtection']

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
		return await self.request_adapter.send_async(request_info, InformationProtectionLabelCollectionResponse, error_mapping)

	async def post(
		self,
		body: InformationProtectionLabel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InformationProtectionLabel:
		"""
		Create new navigation property to labels for me
		
		"""
		tags = ['me.informationProtection']

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
		return await self.request_adapter.send_async(request_info, InformationProtectionLabel, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LabelsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LabelsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LabelsRequest(self.request_adapter, self.path_parameters)

	def by_information_protection_label_id(self,
		informationProtectionLabel_id: str,
	) -> ByInformationProtectionLabelIdRequest:
		if informationProtectionLabel_id is None:
			raise TypeError("informationProtectionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["informationProtectionLabel%2Did"] =  informationProtectionLabel_id

		from .by_information_protection_label_id import ByInformationProtectionLabelIdRequest
		return ByInformationProtectionLabelIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_application(self,
	) -> EvaluateApplicationRequest:
		from .evaluate_application import EvaluateApplicationRequest
		return EvaluateApplicationRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_classification_results(self,
	) -> EvaluateClassificationResultsRequest:
		from .evaluate_classification_results import EvaluateClassificationResultsRequest
		return EvaluateClassificationResultsRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_removal(self,
	) -> EvaluateRemovalRequest:
		from .evaluate_removal import EvaluateRemovalRequest
		return EvaluateRemovalRequest(self.request_adapter, self.path_parameters)

	@property
	def extract_label(self,
	) -> ExtractLabelRequest:
		from .extract_label import ExtractLabelRequest
		return ExtractLabelRequest(self.request_adapter, self.path_parameters)

