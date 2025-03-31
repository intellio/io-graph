from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPublicFolderAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.publicFolderAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.publicFolderAuditRecord")

