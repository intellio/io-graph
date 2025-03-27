from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityLargeContentMetadataAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.largeContentMetadataAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.largeContentMetadataAuditRecord")


