from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class RiskyServicePrincipal(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isProcessing: Optional[bool] = Field(default=None,alias="isProcessing",)
	riskDetail: Optional[RiskDetail] = Field(default=None,alias="riskDetail",)
	riskLastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="riskLastUpdatedDateTime",)
	riskLevel: Optional[RiskLevel] = Field(default=None,alias="riskLevel",)
	riskState: Optional[RiskState] = Field(default=None,alias="riskState",)
	servicePrincipalType: Optional[str] = Field(default=None,alias="servicePrincipalType",)
	history: Optional[list[RiskyServicePrincipalHistoryItem]] = Field(default=None,alias="history",)

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
			if mapping_key == "#microsoft.graph.riskyServicePrincipalHistoryItem":
				from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
				return RiskyServicePrincipalHistoryItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem

