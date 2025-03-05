from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RiskyUser(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted",default=None,)
	isProcessing: Optional[bool] = Field(alias="isProcessing",default=None,)
	riskDetail: Optional[str | RiskDetail] = Field(alias="riskDetail",default=None,)
	riskLastUpdatedDateTime: Optional[datetime] = Field(alias="riskLastUpdatedDateTime",default=None,)
	riskLevel: Optional[str | RiskLevel] = Field(alias="riskLevel",default=None,)
	riskState: Optional[str | RiskState] = Field(alias="riskState",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	history: Optional[list[RiskyUserHistoryItem]] = Field(alias="history",default=None,)

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
			if mapping_key == "#microsoft.graph.riskyUserHistoryItem":
				from .risky_user_history_item import RiskyUserHistoryItem
				return RiskyUserHistoryItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risky_user_history_item import RiskyUserHistoryItem

