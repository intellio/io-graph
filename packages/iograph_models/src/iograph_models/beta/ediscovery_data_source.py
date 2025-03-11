from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryDataSource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	holdStatus: Optional[EdiscoveryDataSourceHoldStatus | str] = Field(alias="holdStatus",default=None,)

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
			if mapping_key == "#microsoft.graph.ediscovery.siteSource":
				from .ediscovery_site_source import EdiscoverySiteSource
				return EdiscoverySiteSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.unifiedGroupSource":
				from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
				return EdiscoveryUnifiedGroupSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.userSource":
				from .ediscovery_user_source import EdiscoveryUserSource
				return EdiscoveryUserSource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .ediscovery_data_source_hold_status import EdiscoveryDataSourceHoldStatus

