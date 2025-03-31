from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDlpSensitiveInformationTypeCmdletRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dlpSensitiveInformationTypeCmdletRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dlpSensitiveInformationTypeCmdletRecord")

