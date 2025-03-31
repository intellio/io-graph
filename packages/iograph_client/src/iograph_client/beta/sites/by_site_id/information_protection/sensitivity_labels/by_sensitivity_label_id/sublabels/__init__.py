# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .evaluate import EvaluateRequest
	from .count import CountRequest
	from .by_sensitivity_label_id1 import BySensitivityLabelId1Request
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.sensitivity_label_collection_response import SensitivityLabelCollectionResponse
from iograph_models.beta.sensitivity_label import SensitivityLabel
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SublabelsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/informationProtection/sensitivityLabels/{sensitivityLabel%2Did}/sublabels", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SensitivityLabelCollectionResponse:
		"""
		Get sublabels from sites
		
		"""
		tags = ['sites.informationProtection']

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
		return await self.request_adapter.send_async(request_info, SensitivityLabelCollectionResponse, error_mapping)

	async def post(
		self,
		body: SensitivityLabel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SensitivityLabel:
		"""
		Create new navigation property to sublabels for sites
		
		"""
		tags = ['sites.informationProtection']

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
		return await self.request_adapter.send_async(request_info, SensitivityLabel, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SublabelsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SublabelsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SublabelsRequest(self.request_adapter, self.path_parameters)

	def by_sensitivity_label_id1(self,
		site_id: str,
		sensitivityLabel_id: str,
		sensitivityLabel_id1: str,
	) -> BySensitivityLabelId1Request:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if sensitivityLabel_id is None:
			raise TypeError("sensitivityLabel_id cannot be null.")
		if sensitivityLabel_id1 is None:
			raise TypeError("sensitivityLabel_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["sensitivityLabel%2Did"] =  sensitivityLabel_id
		path_parameters["sensitivityLabel%2Did1"] =  sensitivityLabel_id1

		from .by_sensitivity_label_id1 import BySensitivityLabelId1Request
		return BySensitivityLabelId1Request(self.request_adapter, path_parameters)

	def count(self,
		site_id: str,
		sensitivityLabel_id: str,
	) -> CountRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if sensitivityLabel_id is None:
			raise TypeError("sensitivityLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["sensitivityLabel%2Did"] =  sensitivityLabel_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def evaluate(self,
		site_id: str,
		sensitivityLabel_id: str,
	) -> EvaluateRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if sensitivityLabel_id is None:
			raise TypeError("sensitivityLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["sensitivityLabel%2Did"] =  sensitivityLabel_id

		from .evaluate import EvaluateRequest
		return EvaluateRequest(self.request_adapter, path_parameters)

