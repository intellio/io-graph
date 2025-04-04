from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftPurviewPolicyOperationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftPurviewPolicyOperationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftPurviewPolicyOperationRecord")

