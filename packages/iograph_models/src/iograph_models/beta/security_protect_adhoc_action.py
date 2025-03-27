from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProtectAdhocAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.protectAdhocAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.protectAdhocAction")


