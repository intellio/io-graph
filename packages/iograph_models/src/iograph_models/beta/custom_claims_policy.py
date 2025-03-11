from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	audienceOverride: Optional[str] = Field(alias="audienceOverride",default=None,)
	claims: SerializeAsAny[Optional[list[CustomClaimBase]]] = Field(alias="claims",default=None,)
	includeApplicationIdInIssuer: Optional[bool] = Field(alias="includeApplicationIdInIssuer",default=None,)
	includeBasicClaimSet: Optional[bool] = Field(alias="includeBasicClaimSet",default=None,)

from .custom_claim_base import CustomClaimBase

