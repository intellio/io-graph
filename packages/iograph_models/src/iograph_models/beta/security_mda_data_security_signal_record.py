from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMdaDataSecuritySignalRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mdaDataSecuritySignalRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mdaDataSecuritySignalRecord")


