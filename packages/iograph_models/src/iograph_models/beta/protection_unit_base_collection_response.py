from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class ProtectionUnitBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DriveProtectionUnit, MailboxProtectionUnit, SiteProtectionUnit],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .drive_protection_unit import DriveProtectionUnit
from .mailbox_protection_unit import MailboxProtectionUnit
from .site_protection_unit import SiteProtectionUnit
