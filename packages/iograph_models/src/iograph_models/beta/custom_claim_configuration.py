from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimConfiguration(BaseModel):
	attribute: SerializeAsAny[Optional[CustomClaimAttributeBase]] = Field(alias="attribute",default=None,)
	condition: SerializeAsAny[Optional[CustomClaimConditionBase]] = Field(alias="condition",default=None,)
	transformations: SerializeAsAny[Optional[list[CustomClaimTransformation]]] = Field(alias="transformations",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_claim_attribute_base import CustomClaimAttributeBase
from .custom_claim_condition_base import CustomClaimConditionBase
from .custom_claim_transformation import CustomClaimTransformation

