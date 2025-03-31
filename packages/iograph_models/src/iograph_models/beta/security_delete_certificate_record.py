from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDeleteCertificateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.deleteCertificateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.deleteCertificateRecord")

