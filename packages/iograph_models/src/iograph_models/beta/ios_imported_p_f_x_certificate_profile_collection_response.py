from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosImportedPFXCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosImportedPFXCertificateProfile]] = Field(alias="value", default=None,)

from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile

