from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class RemoveProtectionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.removeProtectionAction"] = Field(alias="@odata.type", default="#microsoft.graph.removeProtectionAction")


