from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppDetectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Win32LobAppFileSystemDetection, Win32LobAppPowerShellScriptDetection, Win32LobAppProductCodeDetection, Win32LobAppRegistryDetection],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection

