from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequestRemoteHelpSessionAccessResponse(BaseModel):
	pubSubEncryption: Optional[str] = Field(alias="pubSubEncryption",default=None,)
	pubSubEncryptionKey: Optional[str] = Field(alias="pubSubEncryptionKey",default=None,)
	sessionKey: Optional[str] = Field(alias="sessionKey",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


