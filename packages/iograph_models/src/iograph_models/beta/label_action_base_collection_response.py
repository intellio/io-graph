from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class LabelActionBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[EncryptWithTemplate, EncryptWithUserDefinedRights, AddFooter, AddHeader, AddWatermark, ProtectGroup, ProtectOnlineMeetingAction, ProtectSite],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .encrypt_with_template import EncryptWithTemplate
from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
from .add_footer import AddFooter
from .add_header import AddHeader
from .add_watermark import AddWatermark
from .protect_group import ProtectGroup
from .protect_online_meeting_action import ProtectOnlineMeetingAction
from .protect_site import ProtectSite
