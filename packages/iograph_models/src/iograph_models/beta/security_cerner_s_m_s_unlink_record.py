from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCernerSMSUnlinkRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cernerSMSUnlinkRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cernerSMSUnlinkRecord")

