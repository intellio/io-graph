from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsKioskAppBase(BaseModel):
	appType: Optional[WindowsKioskAppType | str] = Field(alias="appType", default=None,)
	autoLaunch: Optional[bool] = Field(alias="autoLaunch", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	startLayoutTileSize: Optional[WindowsAppStartLayoutTileSize | str] = Field(alias="startLayoutTileSize", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.windowsKioskDesktopApp":
				from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
				return WindowsKioskDesktopApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskUWPApp":
				from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
				return WindowsKioskUWPApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskWin32App":
				from .windows_kiosk_win32_app import WindowsKioskWin32App
				return WindowsKioskWin32App.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .windows_kiosk_app_type import WindowsKioskAppType
from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize
