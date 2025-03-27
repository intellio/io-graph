from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAipSensitivityLabelActionLogRequest(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aipSensitivityLabelActionLogRequest"] = Field(alias="@odata.type", default="#microsoft.graph.security.aipSensitivityLabelActionLogRequest")


