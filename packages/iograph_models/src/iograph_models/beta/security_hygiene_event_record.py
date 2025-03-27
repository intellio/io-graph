from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHygieneEventRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.hygieneEventRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.hygieneEventRecord")


