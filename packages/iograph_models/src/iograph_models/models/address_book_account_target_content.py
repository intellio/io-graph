from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddressBookAccountTargetContent(BaseModel):
	type: Optional[str | AccountTargetContentType] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accountTargetEmails: Optional[list[str]] = Field(alias="accountTargetEmails",default=None,)

from .account_target_content_type import AccountTargetContentType

