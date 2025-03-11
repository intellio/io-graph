from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EncryptWithTemplate(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	encryptWith: Optional[EncryptWith | str] = Field(alias="encryptWith",default=None,)
	availableForEncryption: Optional[bool] = Field(alias="availableForEncryption",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)

from .encrypt_with import EncryptWith

