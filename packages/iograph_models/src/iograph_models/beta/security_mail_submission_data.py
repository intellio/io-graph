from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMailSubmissionData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mailSubmissionData"] = Field(alias="@odata.type", default="#microsoft.graph.security.mailSubmissionData")


