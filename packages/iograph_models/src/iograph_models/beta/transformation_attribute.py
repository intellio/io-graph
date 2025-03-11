from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TransformationAttribute(BaseModel):
	attribute: SerializeAsAny[Optional[CustomClaimAttributeBase]] = Field(alias="attribute",default=None,)
	treatAsMultiValue: Optional[bool] = Field(alias="treatAsMultiValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_claim_attribute_base import CustomClaimAttributeBase

