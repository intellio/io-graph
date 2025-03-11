from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EncryptWithUserDefinedRights(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	encryptWith: Optional[EncryptWith | str] = Field(alias="encryptWith",default=None,)
	allowAdHocPermissions: Optional[bool] = Field(alias="allowAdHocPermissions",default=None,)
	allowMailForwarding: Optional[bool] = Field(alias="allowMailForwarding",default=None,)
	decryptionRightsManagementTemplateId: Optional[str] = Field(alias="decryptionRightsManagementTemplateId",default=None,)

from .encrypt_with import EncryptWith

