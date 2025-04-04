from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDownloadCertificateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.downloadCertificateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.downloadCertificateRecord")

