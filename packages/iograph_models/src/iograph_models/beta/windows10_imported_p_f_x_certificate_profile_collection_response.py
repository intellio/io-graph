from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10ImportedPFXCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10ImportedPFXCertificateProfile]] = Field(alias="value", default=None,)

from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
