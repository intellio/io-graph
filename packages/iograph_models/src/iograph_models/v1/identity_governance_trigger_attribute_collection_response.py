from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTriggerAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityGovernanceTriggerAttribute]] = Field(alias="value", default=None,)

from .identity_governance_trigger_attribute import IdentityGovernanceTriggerAttribute
