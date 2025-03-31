from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class Import_apple_device_identity_listPostRequest(BaseModel):
	importedAppleDeviceIdentities: Optional[list[Annotated[Union[ImportedAppleDeviceIdentityResult],Field(discriminator="odata_type")]]] = Field(alias="importedAppleDeviceIdentities", default=None,)
	overwriteImportedDeviceIdentities: Optional[bool] = Field(alias="overwriteImportedDeviceIdentities", default=None,)

from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
