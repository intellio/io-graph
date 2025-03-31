from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class EdiscoveryDataSourceContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	holdStatus: Optional[EdiscoveryDataSourceHoldStatus | str] = Field(alias="holdStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime", default=None,)
	status: Optional[EdiscoveryDataSourceContainerStatus | str] = Field(alias="status", default=None,)
	lastIndexOperation: Optional[EdiscoveryCaseIndexOperation] = Field(alias="lastIndexOperation", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.ediscovery.custodian":
				from .ediscovery_custodian import EdiscoveryCustodian
				return EdiscoveryCustodian.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.noncustodialDataSource":
				from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
				return EdiscoveryNoncustodialDataSource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .ediscovery_data_source_hold_status import EdiscoveryDataSourceHoldStatus
from .ediscovery_data_source_container_status import EdiscoveryDataSourceContainerStatus
from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
