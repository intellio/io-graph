from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AddressBookAccountTargetContent(BaseModel):
	type: Optional[AccountTargetContentType | str] = Field(alias="type", default=None,)
	odata_type: Literal["#microsoft.graph.addressBookAccountTargetContent"] = Field(alias="@odata.type", default="#microsoft.graph.addressBookAccountTargetContent")
	accountTargetEmails: Optional[list[str]] = Field(alias="accountTargetEmails", default=None,)

from .account_target_content_type import AccountTargetContentType
