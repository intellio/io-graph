from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class RiskyServicePrincipal(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isProcessing: Optional[bool] = Field(alias="isProcessing", default=None,)
	riskDetail: Optional[RiskDetail | str] = Field(alias="riskDetail", default=None,)
	riskLastUpdatedDateTime: Optional[datetime] = Field(alias="riskLastUpdatedDateTime", default=None,)
	riskLevel: Optional[RiskLevel | str] = Field(alias="riskLevel", default=None,)
	riskState: Optional[RiskState | str] = Field(alias="riskState", default=None,)
	servicePrincipalType: Optional[str] = Field(alias="servicePrincipalType", default=None,)
	history: Optional[list[RiskyServicePrincipalHistoryItem]] = Field(alias="history", default=None,)

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
