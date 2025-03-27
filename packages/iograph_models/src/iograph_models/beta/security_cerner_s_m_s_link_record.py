from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCernerSMSLinkRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cernerSMSLinkRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cernerSMSLinkRecord")


