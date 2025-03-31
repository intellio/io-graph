from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityUploadCertificateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.uploadCertificateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.uploadCertificateRecord")

