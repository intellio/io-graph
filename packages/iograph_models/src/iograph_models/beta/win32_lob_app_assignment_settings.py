from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.win32LobAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppAssignmentSettings")
	autoUpdateSettings: Optional[Win32LobAppAutoUpdateSettings] = Field(alias="autoUpdateSettings", default=None,)
	deliveryOptimizationPriority: Optional[Win32LobAppDeliveryOptimizationPriority | str] = Field(alias="deliveryOptimizationPriority", default=None,)
	installTimeSettings: Optional[MobileAppInstallTimeSettings] = Field(alias="installTimeSettings", default=None,)
	notifications: Optional[Win32LobAppNotification | str] = Field(alias="notifications", default=None,)
	restartSettings: Optional[Win32LobAppRestartSettings] = Field(alias="restartSettings", default=None,)

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
			if mapping_key == "#microsoft.graph.win32CatalogAppAssignmentSettings":
				from .win32_catalog_app_assignment_settings import Win32CatalogAppAssignmentSettings
				return Win32CatalogAppAssignmentSettings.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
from .win32_lob_app_notification import Win32LobAppNotification
from .win32_lob_app_restart_settings import Win32LobAppRestartSettings

