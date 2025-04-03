from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class RestorePoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.restorePoint"] = Field(alias="@odata.type", default="#microsoft.graph.restorePoint")
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	protectionDateTime: Optional[datetime] = Field(alias="protectionDateTime", default=None,)
	tags: Optional[RestorePointTags | str] = Field(alias="tags", default=None,)
	protectionUnit: Optional[Union[DriveProtectionUnit, MailboxProtectionUnit, SiteProtectionUnit]] = Field(alias="protectionUnit", default=None,discriminator="odata_type", )

from .restore_point_tags import RestorePointTags
from .drive_protection_unit import DriveProtectionUnit
from .mailbox_protection_unit import MailboxProtectionUnit
from .site_protection_unit import SiteProtectionUnit
