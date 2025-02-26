from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityDataSource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	holdStatus: Optional[SecurityDataSourceHoldStatus] = Field(default=None,alias="holdStatus",)

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
			if mapping_key == "#microsoft.graph.security.siteSource":
				from .security_site_source import SecuritySiteSource
				return SecuritySiteSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unifiedGroupSource":
				from .security_unified_group_source import SecurityUnifiedGroupSource
				return SecurityUnifiedGroupSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.userSource":
				from .security_user_source import SecurityUserSource
				return SecurityUserSource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .security_data_source_hold_status import SecurityDataSourceHoldStatus

