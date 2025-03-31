from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftPurviewDataMapOperationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftPurviewDataMapOperationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftPurviewDataMapOperationRecord")

