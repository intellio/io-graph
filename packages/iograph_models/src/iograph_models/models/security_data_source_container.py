from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataSourceContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	holdStatus: Optional[SecurityDataSourceHoldStatus] = Field(default=None,alias="holdStatus",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	releasedDateTime: Optional[datetime] = Field(default=None,alias="releasedDateTime",)
	status: Optional[SecurityDataSourceContainerStatus] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.security.ediscoveryCustodian":
				from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
				return SecurityEdiscoveryCustodian.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryNoncustodialDataSource":
				from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
				return SecurityEdiscoveryNoncustodialDataSource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus

