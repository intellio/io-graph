from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[OmaSettingBase64, OmaSettingBoolean, OmaSettingDateTime, OmaSettingFloatingPoint, OmaSettingInteger, OmaSettingString, OmaSettingStringXml],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .oma_setting_base64 import OmaSettingBase64
from .oma_setting_boolean import OmaSettingBoolean
from .oma_setting_date_time import OmaSettingDateTime
from .oma_setting_floating_point import OmaSettingFloatingPoint
from .oma_setting_integer import OmaSettingInteger
from .oma_setting_string import OmaSettingString
from .oma_setting_string_xml import OmaSettingStringXml

